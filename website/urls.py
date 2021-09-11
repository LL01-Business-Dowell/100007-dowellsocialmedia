from django.contrib import admin
from django.urls import path

from website import views

urlpatterns = [
    path('', views.index),
    path('submit/', views.FormWizard.as_view()),
]
