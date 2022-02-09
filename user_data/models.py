import random

from django.contrib.auth import password_validation
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.db import models
from rest_framework import serializers

from .manager import CustomManager


# Create your models here.
class UserTable(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100, null=False, blank=False,
                                validators=[RegexValidator(r'[A-Za-z0-9@#$%^&+=]{8,}',
                                                           message='Must have atleast one: A-Z,a-z,0-9,sp. character')])
    first_name = None
    last_name = None
    firstName = models.CharField(max_length=150, blank=True)
    lastName = models.CharField(max_length=150, blank=True)
    player_name = models.CharField(max_length=150)
    user_id = models.PositiveBigIntegerField(unique=True, blank=False, null=True)
    team_name = models.CharField(max_length=150, unique=True, blank=False, null=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomManager()

    def __str__(self):
        return str(self.first_name)

       # def get_user_id(self):
    #     return self.id + 10000000
    #     # return self.id+10000000
    #
    # def GetUserID(self):
    #     pass

    # def save(self, *args, **kwargs):
    #     user=super().save(*args, **kwargs)
    #     user.user_id = self.get_user_id()
    #     user.save(*args, **kwargs)
    #     if self._password is not None:
    #         password_validation.password_changed(self._password, self)
    #         self._password = None
    #
    #     if self.user_id is not None:
    #         UserTable.user_id = self.user_id
