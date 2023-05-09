from django.urls import path
from . import views

urlpatterns = [
    path('github/token', views.github_token_exchange,
         name='github_token_exchange'),
]
