from django.contrib import admin

# Register your models here.
from .models import agegroup, batches, teachers, timings, days

admin.site.register(agegroup)
admin.site.register(batches)
admin.site.register(teachers)
admin.site.register(timings)
admin.site.register(days)