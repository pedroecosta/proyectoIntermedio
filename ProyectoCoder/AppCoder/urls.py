from django.urls import path
from AppCoder import views


urlpatterns = [
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('usuarios', views.usuarios, name="Usuarios"),
    path('deportes', views.deportes, name="Deportes"),
    path('politica', views.politica, name="Politica"),
    path('arte', views.arte, name="Arte"),
    path('busquedaComentario', views.busquedaComentario, name="Busqueda de Comentarios"),
    path('buscar/', views.buscar),
]