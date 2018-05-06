from django.conf.urls import url
from AppFive import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]