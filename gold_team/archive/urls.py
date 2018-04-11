from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostListView.as_view(), name='feed'),
    #path('post/<int:pk>', views.PostListView.as_view(), name='post'),
    #path('home/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    #path('profile/login/', views.login, name='login'),
]

urlpatterns += [   
    path('myposts/', views.PostsByUserListView.as_view(), name='my-borrowed'),
]