from django.urls import path, include
from rest_framework import views
from . import views

urlpatterns = [
   
    path(r'^$', views.api_root),
    path(r'albums/$', views.AlbumList.as_view(), name='album-list'),
    path(r'albums/(?P<pk>[0-9]+)/$', views.AlbumDetail.as_view()),
    path(r'photos/$', views.PhotoList.as_view(), name='photo-list'),
    path(r'photos/(?P<pk>[0-9]+)/$', views.PhotoDetail.as_view()),
    path(r'users/$', views.UserList.as_view(), name='user-list'),
    path(r'users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    
    path(r'api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]

