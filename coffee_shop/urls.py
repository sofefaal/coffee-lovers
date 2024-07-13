from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='coffee-home'),
    path('about/', views.about, name='coffee-about'),
    path('posts/', views.posts, name='coffee-posts')
]