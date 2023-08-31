from django.shortcuts import render, get_object_or_404, redirect
from .models import batches, agegroup, days, timings
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import BatchForm
from django.contrib.auth.decorators import login_required
import json
from django.http import HttpResponse
from django.contrib import messages
from django.utils.text import slugify
from .filters import batchfilter
from .googlesheet import writedata
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log in the user
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('frontpage')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})

def logout_view(request):
        logout(request)
        return redirect('frontpage')
# Create your views here.
def frontpage(request):
    Batches = batches.objects.all()

    return render(request, 'core/index.html', {
        'Batches': Batches
    })
@login_required
def batch_detail(request,agegroup_slug, slug):
    Batch = get_object_or_404(batches, slug=slug)

    return render(request, 'core/batch_detail.html', {
        'batch': Batch
    })
@login_required
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
@login_required
def agegroup_detail(request, slug):
    Agegroup = get_object_or_404(agegroup, slug=slug)
    batch = Agegroup.agegroups.all()
    Batch=batch.filter()
    return render(request, 'core/agegroup_detail.html', {
        'Age': Agegroup,
        'Batch': Batch
    })
@login_required
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
@login_required
def search(request):
    batch_filter=batchfilter(request.GET, queryset=batches.objects.all())
    context={
        'form': batch_filter.form,
        'Batch': batch_filter.qs
    }
    return render(request,'core/search.html',context) 
@login_required
def vacant_detail(request, slug):
    Agegroup = get_object_or_404(agegroup, slug=slug)
    batch = Agegroup.agegroups.all()
    Batch=batch.filter(vacancy=batches.VACANT)
    return render(request, 'core/agegroup_detail.html', {
        'Age': Agegroup,
        'Batch': Batch
    })
@login_required
def savedata(request, pk):
    batch = batches.objects.get(pk=pk)
    print(batch.batch_name,batch.batch_size,batch.timing,batch.days,batch.strength,batch.startdate,batch.teachername,batch.agegroup,batch.description,batch.status,batch.vacancy)
    a=[batch.batch_name,batch.batch_size,batch.timing,batch.days,batch.strength,batch.startdate,batch.teachername,batch.agegroup,batch.description,batch.status,batch.vacancy]
    writedata(a)
    return redirect('frontpage')
