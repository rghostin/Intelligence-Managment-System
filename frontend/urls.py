from django.conf import settings
from django.urls import path, include, re_path
from frontend import views

urlpatterns = [
   path('search', views.search, name='search')
]