# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm

# Create your views here.


def index(request):
    return render(request, 'basic_app/index.html')


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()                       # Here we are grabbing the user for and saving to the database
            user.set_password(user.password)              # Hashing the password by set_password method
            user.save()                                   # Saving the hash password to the database
            # Now dealing with the extra information website link and profile picture
            profile = profile_form.save(commit=False)
            # Commit false saves the collision from the same user information
            profile.user = user

            if 'profile_pic' in request.FILES:            # Check out the actually provided profile picture.
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'basic_app/registration.html', {'user_form': user_form,
                                                           'profile_form': profile_form,
                                                           'registered': registered})


