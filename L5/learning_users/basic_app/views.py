# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# login_required creates the view requred for the login page

# Create your views here.


def index(request):
    return render(request, 'basic_app/index.html')


@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


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


# Login views

def user_login(request):

    if request.method == "POST":    # If the user has filled up the login information
        username = request.POST.get('username')  # Now get the username and password supplied
        # .get('username'): in login.html file in the input the name is username
        password = request.POST.get('password')
        # Now using the django's built in authentication information function to authenticate the user.
        user = authenticate(username=username, password=password)

        if user:    # If we have a user
            if user.is_active:   # if user is active login the user
                login(request, user)   # passing the request and user object written by authenticate in the login.
                return HttpResponseRedirect(reverse('index'))    # Here send the user to somewhere like home page,
                # profile page etc. Here we are redirecting the to index page/home page.

            else:           # If the account is not active.
                return HttpResponse("Account is not active")

        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password {}".format(username, password))
            return HttpResponse("Invalid login details supplied!")

    else:       # If the user is not submitted anything
        return render(request, 'basic_app/login.html', {})












