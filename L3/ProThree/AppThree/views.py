# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
# from AppThree .models import User
from AppThree.forms import NewUserForm

# Create your views here.


def index(request):
    insert_me = {'inset_me': 'Hello I am from views.py'}
    return render(request, 'AppThree/index.html', context=insert_me)


def users(request):
    form = NewUserForm()     # form is a instance of form class made
    if request.method == "POST":     # if someone hits the submit button on that form and sending information back
        form = NewUserForm(request.POST)   # we pass in the the request.post

        if form.is_valid:
            form.save(commit=True)   # If the form is valid it will save the form.
            return index(request)   # This will take back to home page
        else:
            print('Error form is invalid!')

    return render(request, 'AppThree/users.html', {'form': form})
