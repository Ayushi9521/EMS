from django.db import models

# Create your models here.
class Employee(models.Model):
    Id = models.AutoField(primary_key=True )
    Name  = models.CharField(max_length=50,null=True,blank=True)
    DOB = models.CharField(max_length=50,null=True,blank=True)
    DOJ = models.CharField(max_length=50,null=True,blank=True)
    Department = models.CharField(max_length=50,null=True,blank=True)
    post = models.CharField(max_length=50,null=True,blank=True)
    Address = models.CharField(max_length=100,null=True,blank=True)
    City = models.CharField(max_length=50,null=True,blank=True)
    Country = models.CharField(max_length=50,null=True,blank=True)
    ZipCode = models.IntegerField(null=True,blank=True)
    State = models.CharField(max_length=50,null=True,blank=True)
    Active = models.BooleanField(default=False)
    Leave_count = models.IntegerField(default=0)
    on_leave = models.BooleanField(default=False)
