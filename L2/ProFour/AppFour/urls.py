from django.conf.urls import url
from AppFour import views

urlpatterns = [
    url(r'^$', views.users, name='users')
]