from django.conf.urls import url
from groups import views

app_name = 'groups'

urlpatterns = [
    url(r'^$', views.ListGroups.as_view(), name='all'),
    url(r'^new/$', views.createGroup.as_view(), name='create'),
    url(r'^posts/in/(?P<slug>[-\w]+)/$', views.SingleGroup.as_view(), name='single'),
]