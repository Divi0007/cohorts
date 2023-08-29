from django.shortcuts import render, get_object_or_404, redirect
from .models import batches, agegroup, days, timings
from .forms import BatchForm
from django.contrib import messages
from django.utils.text import slugify
from .filters import batchfilter


# Create your views here.
def frontpage(request):
    Batches = batches.objects.all()

    return render(request, 'core/index.html', {
        'Batches': Batches
    })
def batch_detail(request,agegroup_slug, slug):
    Batch = get_object_or_404(batches, slug=slug)

    return render(request, 'core/batch_detail.html', {
        'batch': Batch
    })

def edit_batch(request, pk):
    batch = batches.objects.get(pk=pk)

    if request.method == 'POST':
        form = BatchForm(request.POST, request.FILES, instance=batch)

        if form.is_valid():
            form.save()

            messages.success(request, 'The changes was saved!')

            return redirect('frontpage')
    else:
        form = BatchForm(instance=batch)

    return render(request, 'core/batch_form.html', {
        'title': 'Edit product',
        'product': batch,
        'form': form
    })

def agegroup_detail(request, slug):
    Agegroup = get_object_or_404(agegroup, slug=slug)
    batch = Agegroup.agegroups.all()
    Batch=batch.filter()
    return render(request, 'core/agegroup_detail.html', {
        'Age': Agegroup,
        'Batch': Batch
    })

def add_batch(request):
    if request.method == 'POST':
        form = BatchForm(request.POST, request.FILES)

        if form.is_valid():
            title = request.POST.get('batch_name')

            batch = form.save(commit=False)
            batch.slug = slugify(title)
            batch.save()

            messages.success(request, 'The Batch was added!')

            return redirect('frontpage')
    else:
        form = BatchForm()

    return render(request, 'core/batch_form.html', {
        'title': 'Add Batch',
        'form': form
    })

def search(request):
    batch_filter=batchfilter(request.GET, queryset=batches.objects.all())
    context={
        'form': batch_filter.form,
        'Batch': batch_filter.qs
    }
    return render(request,'core/search.html',context) 

def vacant_detail(request, slug):
    Agegroup = get_object_or_404(agegroup, slug=slug)
    batch = Agegroup.agegroups.all()
    Batch=batch.filter(vacancy=batches.VACANT)
    return render(request, 'core/agegroup_detail.html', {
        'Age': Agegroup,
        'Batch': Batch
    })
