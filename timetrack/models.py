from django.db import models
from django.contrib.auth.models import User

class WorkEntry(models.Model):
    user = models.ForeignKey(User)
    date = models.DateField()
    time_from = models.TimeField('time started')
    time_to = models.TimeField('time finished')
    comment = models.TextField()
