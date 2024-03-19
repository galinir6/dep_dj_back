from django.contrib import admin
from django.urls import path

from base import views

urlpatterns = [
    path('', views.index),
    path('login', views.MyTokenObtainPairView.as_view()),
    path('register',views.register),
    path('getProducts', views.getProducts),
    path('getProducts/<int:id>', views.getProducts),
    path('upload',views.APIViews.as_view()),

]