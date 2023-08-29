from django import forms

from .models import batches

class BatchForm(forms.ModelForm):
    class Meta:
        model = batches
        fields = ('batch_name','batch_size','timing','days','strength','startdate','teachername','agegroup','description','status','vacancy')
        widgets = {
            'agegroup': forms.Select(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'batch_name': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'batch_size': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'days': forms.Select(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'timing': forms.Select(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'strength': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'startdate': forms.TextInput(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'teachername': forms.Select(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'status': forms.Select(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            'vacancy': forms.Select(attrs={
                'class': 'w-full p-4 border border-gray-200'
            }),
            
        }
