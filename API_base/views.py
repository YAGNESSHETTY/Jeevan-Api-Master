from django.shortcuts import render
from django.contrib import admin
from django.urls import path,include

# Create your views here.

path=[
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
