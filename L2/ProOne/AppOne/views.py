# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.


def index(request):
    my_dict = {'insert_content': 'Hello I am from AppOne/views.py!'}
    return render(request, 'AppOne/index.html', context=my_dict)