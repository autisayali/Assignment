from django.db import models


# Create your models here.
class Entry(models.Model):
    uname=models.CharField(max_length=10,primary_key=True)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=5)
    
from Application.models import Entry
class Task(models.Model):
    ID=models.IntegerField(primary_key=True)
    Status=models.CharField(max_length=20)
    Division=models.CharField(max_length=50)
    Category=models.CharField(max_length=20)
    Priority=models.CharField(max_length=10)
    Department=models.CharField(max_length=30)


    