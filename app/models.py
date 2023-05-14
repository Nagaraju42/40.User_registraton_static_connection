from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class ProfileForm(models.ModelForm):
    address=models.TextField()
    profile_pic=models.ImageField(upload_to='pp')