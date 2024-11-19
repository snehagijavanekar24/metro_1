from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Member(models.Model):
    Name=models.CharField(max_length=50)
    Surname=models.CharField(max_length=50)
    Email=models.EmailField()
    Mobile_Number=models.IntegerField()
    D_O_B=models.DateField()
    Age=models.IntegerField()
    Height=models.FloatField()
    Blood_Groop=models.CharField(max_length=20)
    Gender=models.CharField(max_length=50)
    Country=models.CharField(max_length=50)
    State=models.CharField(max_length=50)
    City=models.CharField(max_length=50)
    Address=models.CharField(max_length=50)
    Zipcode=models.IntegerField()
    Profile_Created_By=models.CharField(max_length=50)
    Marital_Status=models.CharField(max_length=50)
    Education=models.CharField(max_length=50)
    Occupation=models.CharField(max_length=50)
    Income=models.IntegerField()
    Religion=models.CharField(max_length=50)
    Caste=models.CharField(max_length=50)
    Sub_caste=models.CharField(max_length=50)
    About_yourself=models.CharField(max_length=100)
    Image=models.IntegerField()