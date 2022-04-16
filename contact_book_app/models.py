from django.db import models
from django import forms
from django.conf import settings
from django.contrib.auth.models import User


User = settings.AUTH_USER_MODEL

# class User(models.Model):
#     username = models.CharField(max_length=100)
#     email= models.CharField(max_length=500)
#     password1= models.CharField(max_length=30)
#     password2= models.CharField(max_length=30)


class ContactDetail(models.Model):
    name = models.CharField(max_length=200)
    profile= models.ImageField(upload_to='images/',null=True, blank=True)
    mobile_no = models.IntegerField()
    address= models.TextField(max_length=400)
    email= models.CharField(max_length=500)
    user = models.ForeignKey(User,default=1, null=True, on_delete= models.SET_NULL)


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email