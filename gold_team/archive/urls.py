from django.urls import path
from . import views


urlpatterns = [
    path('', views.feed, name='feed'),
    path('feed/', views.PostListView.as_view(), name='post'),
    path('feed/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    path('login/', views.login, name='login'),
    #path('profile/login/', views.login, name='login'),
]
