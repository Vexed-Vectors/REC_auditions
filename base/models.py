from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Experience(models.Model):
    user = models.ForeignKey( User,on_delete = models.CASCADE)
    post = models.CharField(max_length=100, blank=False, null=True)
    company = models.CharField(max_length=100, blank=False, null=True )
    date_added = models.DateTimeField(auto_now_add= True)
    content = models.CharField(max_length=500, null=True, blank=False)
    is_approved = models.BooleanField(default= False, null=True, blank=True)
    
    duration = models.CharField(max_length=20, null=True, blank=False)

