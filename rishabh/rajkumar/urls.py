from django.conf.urls import url
from rajkumar import views

urlpatterns = [

    url('$', views.HomePageView.as_view()),
]