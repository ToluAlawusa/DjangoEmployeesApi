from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Employee(models.Model):
    fullname = models.CharField(max_length = 100)
    emp_code = models.CharField(max_length = 3)
    mobile = models.CharField(max_length = 11)