"""simplesocial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from simplesocial import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    # connecting the accounts main space to accounts.urls, if someone login or signup that connects directly to urls.py
    # file in the accounts application.
    url(r'^accounts/', include('django.contrib.auth.urls')),  # django.contrib.urls allows everything that django has
    # under the hood for authorization
    url(r'^test/$', views.TestPage.as_view(), name='test'),
    url(r'^thanks/$', views.ThanksPage.as_view(), name='thanks'),
    url(r'^posts/', include('posts.urls', namespace='posts')),
    url(r'^groups/', include('groups.urls', namespace='groups')),


]
