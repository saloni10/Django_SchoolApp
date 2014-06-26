from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20)
    roll_no = models.IntegerField(max_length=20)
    branch = models.CharField(max_length=20)
    session = models.IntegerField(max_length=20)
    marks = models.IntegerField(max_length=20)
    backlog = models.CharField(max_length=20)
    def __str__(self):
        return self.name