from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# Create your models here.

class User(AbstractBaseUser):
  email = models.EmailField(
    verbose_name='email address',
    max_length= 225,
    unique=True,
  ),
  identifier = models.CharField(max_length=40, unique=True)

  wins = models.IntegerField()
  losses = models.IntegerField()
  draws = models.IntegerField()

  active = models.BooleanField(default=True)
  staff = models.BooleanField(default=False)
  admin = models.BooleanField(default=False)
  friends = models.ManyToManyField('User', blank=True)

  USERNAME_FIELD = 'identifier'
  REQUIRED_FIELDS = [email]



  class Friend_Request(models.Model):
    from_user = models.ForeignKey(
      User, related_name='from_user', on_delete=models.CASCADE)
    
    to_user = models.ForeignKey(
      User, related_name='to_user', on_delete=models.CASCADE)
    