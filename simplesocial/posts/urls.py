from django.contrib.urls import url
from posts import views

app_name = 'posts'

urlpatterns = [
    url(r'^$', views.PostList.as_view(), name='all'),
    url(r'^new/$', views.CreatePost.as_view(), name='create'),
    url(r'^by/(?P<username>[-\w]+)$', views.UserPosts.as_view(), name='for_user'),
    url(r'^by/(?P<username>[-\w]+)$', views.PostDetail.as_view(), name='single'),
    url(r'^delete/(?P<username>[-\w]+)$', views.DeletePost.as_view(), name='delete'),
]
