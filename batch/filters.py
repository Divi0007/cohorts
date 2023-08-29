import django_filters
from .models import batches

class batchfilter(django_filters.FilterSet):
    class Meta:
        model=batches
        fields=['agegroup','days','status','timing','vacancy','startdate']
