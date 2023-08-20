from django.urls import path

from . import views

app_name = 'places'
urlpatterns = [
    path('place/', views.place_request, name='place'),
]
