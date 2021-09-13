from django.conf.urls import url

from website import views

urlpatterns = [
    url('', views.index, name='index'),
]
