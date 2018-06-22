
from django.conf.urls import url
from tree import views

urlpatterns = [
    url('$', views.HomePageView.as_view()),
    url('about/$', views.AboutPageView.as_view()),
]