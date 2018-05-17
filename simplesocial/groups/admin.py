# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from groups import models

# Register your models here.
# Here we will create a tabular inline: in the inline class we will be using basic classes to utilize the admin
# interface to django website with the ability to edit models on the same page on parent model.


class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember


admin.site.register(models.Group)


