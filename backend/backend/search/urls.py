from django.urls import path

from .views import Search

app_name = 'search'
urlpatterns = [
    path('search/<str:query>/', Search.as_view())
]
