from django.conf.urls import url
from basic_app import views


# Template tagging
app_name = 'basic_app'   # for template tagging

urlpatterns = [
    url(r'^relative/$', views.relative, name='relative'),
    url(r'^other/$', views.other, name='other')
]
