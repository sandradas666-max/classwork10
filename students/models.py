
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)
    student_class = models.CharField(max_length=100)
    age = models.IntegerField()

# Create your models here.
