from django.db import models

class User(models.Model):
    group_name = models.CharField(max_length=30)
    start_date = models.DateField()
    interval = models.IntegerField()

