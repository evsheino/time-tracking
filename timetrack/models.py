from django.db import models
from django.contrib.auth.models import User

class WorkEntry(models.Model):
    user = models.ForeignKey(User)
    date = models.DateField('päivämäärä')
    hours = models.FloatField('tunnit')
    comment = models.TextField('kommentti')

    def __str__(self):
        return "%s %s %s % s" % (self.user, self.date, self.hours, self.comment)
