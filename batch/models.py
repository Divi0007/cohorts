from django.db import models

# Create your models here.
class agegroup(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    
    def __str__(self):
        return self.title
class timings(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    
    def __str__(self):
        return self.title

class days(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    
    def __str__(self):
        return self.title

class teachers(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    
    def __str__(self):
        return self.title

class batches(models.Model):
    DRAFT = 'draft'
    WAITING_APPROVAL = 'waitingapproval'
    ACTIVE = 'active'
    ENDED = 'ended'
    VACANT='VACANT'
    FULL="FULL"
    STATUS_CHOICES = (
        (DRAFT, 'Draft'),
        (WAITING_APPROVAL, 'Waiting approval'),
        (ACTIVE, 'Active'),
        (ENDED, 'Deleted'),
    )
    VACANCY_CHOICE={
        (VACANT,'VACANT'),
        (FULL,'FULL')
    }
    batch_name = models.CharField(max_length=50)
    slug = models.SlugField()
    batch_size = models.IntegerField()
    timing = models.ForeignKey(timings, related_name='Timings', on_delete=models.CASCADE)
    days=models.ForeignKey(days, related_name='Days', on_delete=models.CASCADE)
    strength = models.IntegerField()
    startdate=models.CharField(max_length=50)
    teachername = models.ForeignKey(teachers, related_name='Teachers', on_delete=models.CASCADE)
    agegroup=models.ForeignKey(agegroup, related_name='agegroups', on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=ACTIVE)
    vacancy=models.CharField(max_length=50, choices=VACANCY_CHOICE, default=VACANT)
    def __str__(self):
        return self.batch_name
    
    def get_batchsize(self):
        return str(str(self.strength)+"/"+str(self.batch_size))
    
    def stren(self):
        return ((self.batch_size)-(self.strength))