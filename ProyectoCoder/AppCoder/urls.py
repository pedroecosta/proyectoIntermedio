from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('inicio/', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('usuarios/', views.usuarios, name="Usuarios"),
    path('deportes/', views.deportes, name="Deportes"),
    path('politica/', views.politica, name="Politica"),
    path('arte/', views.arte, name="Arte"),
    path('busquedaComentarioDeporte/', views.busquedaComentarioDeporte, name="Busqueda de Comentarios"),
    path('busquedaComentarioArte/', views.busquedaComentarioArte, name="Busqueda de Comentarios"),
    path('busquedaComentarioPolitica/', views.busquedaComentarioPolitica, name="Busqueda de Comentarios"),
    path('buscarDeporte/', views.buscarDeporte),
    path('buscarArte/', views.buscarArte),
    path('buscarPolitica/', views.buscarPolitica),
    path('login/', views.login_request, name="Login"),
    path('register/', views.register, name='Register'),
    path('logout/', LogoutView.as_view(template_name='AppCoder/logout.html'), name='Logout'),
    path('editarPerfil/', views.editarPerfil, name="EditarPerfil")
]