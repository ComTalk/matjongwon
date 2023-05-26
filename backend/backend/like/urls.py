from django.urls import path
from . import views

app_name = 'like'
urlpatterns = [
    path('like/', views.like_button, name='like'),
    path('dislike/', views.dislike_button, name='dislike'),
]
