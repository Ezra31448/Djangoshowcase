from django.urls import path
from connectdb import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('form', views.form),
]