from django.db import models
from django.db.models.base import Model

# Create your models here.

class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=200)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.ename


