from django.db import models
from django import forms

# # Create your models here.
# class qa(models.Model):
#     question = models.CharField( max_length=100)
#     ans= models.TextField(default='')

class chapter(models.Model):
    id=models.CharField(max_length=25,null=False,blank=True,primary_key=True)
    name=models.TextField(blank=True,null=True)

class topic(models.Model):
    id=models.CharField(max_length=25,null=False,blank=True)
    t_id=models.CharField(max_length=25,null=False,blank=True,primary_key=True)
    name=models.TextField(blank=True,null=True)
    meaning=models.TextField(blank=True,null=True)
    status=models.CharField(max_length=5,null=True,blank=True)

class sub_topic(models.Model):
    t_id=models.CharField(max_length=25,null=False,blank=True)
    s_id=models.CharField(max_length=25,null=False,blank=True,primary_key=True)
    name=models.TextField(blank=True,null=True)
    meaning=models.TextField(blank=True,null=True)
    status=models.CharField(max_length=5,null=True,blank=True)
