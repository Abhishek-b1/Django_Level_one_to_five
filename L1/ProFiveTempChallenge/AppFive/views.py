# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    my_dict = {'insert_me': 'Hello I am from views.py'}
    return render(request, 'AppFive_template/index.html', context=my_dict)
