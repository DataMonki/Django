from django.urls import path

#we import local views to access the function homepageview
from .views import homePageView

urlpatterns = [
    path("",homePageView, name="home")
]