from django.db import models

# Create your models here.
class Members(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  fathername=models.CharField(max_length=255)
  age = models.CharField(max_length=255)
  address = models.CharField(max_length=255)
  email=models.CharField(max_length=255)
  education=models.CharField(max_length=255)
  hobby=models.CharField(max_length=255)