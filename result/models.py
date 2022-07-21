from django.db import models
from django.db.models import Model

# Create your models here.
class Result_Data(models.Model):
    name = models.CharField(max_length=35)
    school = models.CharField(max_length=35)
    rollno = models.CharField(max_length=15)
    gender = models.CharField(max_length=5)
    bengali = models.CharField(max_length=35)
    english = models.CharField(max_length=35)
    mathematic = models.CharField(max_length=35)
    physics = models.CharField(max_length=35)
    chemistry = models.CharField(max_length=35)
    biology = models.CharField(max_length=35)

    def __str__(self):
        return self.rollno
    