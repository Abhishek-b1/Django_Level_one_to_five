from django.conf.urls import url
from AppOne import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]