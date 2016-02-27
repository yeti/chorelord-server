from django.db import models

# Create your models here.

from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=30)
    group_name = models.CharField(max_length=30)
    start_date = models.DateField()
    interval = models.IntegerField()


