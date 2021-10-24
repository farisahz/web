from django.db import models
#from django.db.models.base import Model
from django.db import models
# Create your models here.

class adminuser(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(primary_key=True)
    no_phone = models.CharField(max_length=12)
    password = models.CharField(max_length=200)
    password2 = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username

    
  
