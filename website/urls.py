from django.conf.urls import url
from django.urls import path

from website import views

urlpatterns = [
    path('', views.index, name='index'),
    url('selected_result/', views.selected_result, name='selected_result'),
]
