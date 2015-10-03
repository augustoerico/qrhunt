from django.db import models
from django.contrib.auth.models import User

from base64 import b32encode
from hashlib import sha1
from random import random

def pk_gen():
    return b32encode(sha1(str(random())).digest()).lower()[:6]

class Quest(models.Model):
    master = models.ForeignKey(User)
    
    name = models.CharField(max_length=30)
    
class Hint(models.Model):
    id = models.CharField(max_length=6, primary_key=True, default=pk_gen)
    quest = models.ForeignKey(Quest)
    
    title = models.CharField(max_length=30)
    message = models.CharField(max_length=200)
