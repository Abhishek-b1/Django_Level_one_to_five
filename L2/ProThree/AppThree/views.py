# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from AppThree.models import Topic, Webpage, AccessRecord

# Create your views here.


def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_record': webpages_list}
    # my_dict = {'insert_me': 'Hello I am from views.py!'}
    return render(request, 'AppThree/index.html', context=date_dict)
