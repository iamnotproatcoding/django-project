from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="rubik_shop-home"),
    path("about/", views.about_page, name="rubik_shop-about"),
]