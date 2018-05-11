# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View   # View is the most generic view.

# Create your views here.


class CBView(View):
    def get(self, request):
        return HttpResponse("Class based views are cool!")

