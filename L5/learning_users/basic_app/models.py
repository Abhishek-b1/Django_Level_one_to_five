# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# Here the imported User has already things like username, password, email, first name and last name
# Create your models here.
# The UserProfileInfo class is creating the extra things which the User doesn't contain.


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User)    # OneToOneField is for adding the extra fields for User

    # Additional
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username
