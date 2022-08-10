from django.urls import path,include
from .views import *
urlpatterns = [
    path('', hesaplama, name='ana'),
]
