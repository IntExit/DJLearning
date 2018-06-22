
from django.conf.urls import url
from tree import views

urlpatterns = [
    url('/home', views.home),
    url('/about', views.about),
]