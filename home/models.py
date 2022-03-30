import email
from pyexpat import model
from unicodedata import name
from django.db import models

# Create your models here.

# Models In Django --> Tables --> Sheet

class Contact(models.Model):
    sno = models.AutoField(primary_key = True)
    name= models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    content = models.TextField() 
    timeStemp = models.DateTimeField(auto_now=True,blank=True)


    def __str__(self):
        return 'Message from ' + self.name + ' - ' + self.email 