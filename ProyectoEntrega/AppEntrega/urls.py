from django.urls import path, include
from AppEntrega import views


urlpatterns = [

    path(" ", views.inicio),
    path ("estilo", views.estilo),
    path("truco", views.truco),
    path("mago", views.mago),



]
