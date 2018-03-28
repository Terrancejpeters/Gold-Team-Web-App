from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.PostListView.as_view(), name='post'),
    path('home/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
]
