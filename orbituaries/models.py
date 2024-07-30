from django.db import models
from datetime import datetime

# Create your models here.
class Orbituaries(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    date_of_death = models.DateField()
    content= models.TextField()
    author= models.CharField(max_length=100)
    submission_date = models.DateField(default=datetime.now)
    slug= models.CharField(max_length=255, unique=True, blank=True)


    def __str__(self):
        return self.name