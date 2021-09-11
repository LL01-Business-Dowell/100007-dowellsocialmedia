from django.contrib import admin
from django.urls import path, include
import views as v

urlpatterns = [
    path('', v.index),
]
