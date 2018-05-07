from django.conf.urls import url
from AppThree import views

urlpatterns = [
    url(r'^$', views.users, name='users')
]