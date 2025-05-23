from django.contrib.auth.models import User  
from django.db import models  

class UserProfile(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    is_new_user = models.BooleanField(default=True)  # To track if a user is new  
