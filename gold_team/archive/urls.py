from django.urls import path
from django.conf.urls import include
from . import views


urlpatterns = [
    path('', views.PostListView.as_view(), name='feed'),
    path('feed/', views.PostListView.as_view(), name='post'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
    path('newpost/', views.add_post, name='add_post'),
    path('poll/', views.poll_vote, name='poll_vote'),
    path('poll/results', views.poll_results, name='poll_results'),
]

urlpatterns += [   
    path('myposts/', views.PostsByUserListView.as_view(), name='my-posts'),
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]


