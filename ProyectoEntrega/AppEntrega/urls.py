from django.urls import path, include
from AppEntrega import views


urlpatterns = [

    path('', views.inicio,name="inicio"),
    path ("estilo",views.estilo,name="estilo"),
    path("truco", views.truco,name="truco"),
    path("mago", views.mago,name="mago"),
    #path("estilo-formularios/", views.estilo_formularios,name="estilo-formularios"),
    path("mago-formularios/", views.mago_formularios,name="mago-formularios"),
    #path("truco-formularios/", views.truco_formularios,name="truco-formularios"),
    path ("listado-magos/",views.busqueda_magos, name="listado-magos"),
    #path ("buscar/", views.buscar, name="buscar"),
    path('leerMago', views.leerMago, name = "LeerMago"),
    path('eliminarMago/<Mago_nombre><mago_apellido>',views.eliminarMago, name="eliminarMago"  ),



]