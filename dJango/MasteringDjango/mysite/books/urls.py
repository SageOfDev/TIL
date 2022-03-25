from django.urls import path

from .views import search

app_name = 'books'

urlpatterns = [
    path('search/',
         search),

]