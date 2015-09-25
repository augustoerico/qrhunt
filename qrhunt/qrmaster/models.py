from django.db import models
from django.contrib.auth.models import User

class Quest(models.Model):
    master = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    
class Hint(models.Model):
    title = models.CharField(max_length=30)
    message = models.CharField(max_length=200)
    
    quest = models.ForeignKey(Quest)
