from asyncio.windows_events import NULL
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField
  #Create your models here.




class Profile(models.Model):
   name= models.CharField(max_length=200)
   id2=models.IntegerField()
   age= models.IntegerField()
   occupation=models.CharField(max_length=100)
   place=models.CharField(max_length=20)
   joining_date=models.DateField()
   email_id= models.EmailField(max_length=80)
   profile_Main_Img = models.ImageField(upload_to='images/')