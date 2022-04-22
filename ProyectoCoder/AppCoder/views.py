import re
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.forms import comentarioFormulario, usuarioFormulario
from AppCoder.models import Usuario, Politica, Deportes, Arte
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppCoder.forms import UserRegisterForm, UserEditForm
from django.contrib.auth.decorators import login_required

#vista de registro
def register(request):

      if request.method == "POST":
            form = UserCreationForm(request.POST)
            #form = UserRegisterForm(request.POST)
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()
            return render(request, 'AppCoder/inicio.html', {'mensaje':'Usuario Creado :)'})
      else:
            form = UserCreationForm()
            #form = UserRegisterForm()
      return render(request, 'AppCoder/registro.html', {'form':form})
#vista de login 
def login_request(request):
      if request.method == 'POST':
            form = AuthenticationForm(request, data = request.POST)
            if form.is_valid():
                   # Si pasó la validación de Django
                  usuario = form.cleaned_data.get('username')
                  contrasenia = form.cleaned_data.get('password')
                  
                  user = authenticate(username= usuario, password=contrasenia)
                  if user is not None:
                         login(request, user)
                         return render(request, "AppCoder/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
                  else:
                        return render(request, "AppCoder/inicio.html", {"mensaje":"Datos incorrectos"})
            else:
                 return render(request, "AppCoder/inicio.html", {"mensaje":"Formulario erroneo"})
      form = AuthenticationForm()
      return render(request, "AppCoder/login.html", {"form": form})

@login_required
def inicio(request):

      return render(request, "AppCoder/inicio.html")

def usuarios(request):

      if request.method == 'POST':

            miFormularioUsuario = usuarioFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormularioUsuario)

            if miFormularioUsuario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormularioUsuario.cleaned_data

                  usuario = Usuario (nombre=informacion['Nombre'], apellido=informacion['Apellido'], email=informacion['Email'], contraseña=informacion['Contraseña']) 

                  usuario.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

           miFormularioUsuario= usuarioFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/usuarios.html", {"miFormularioUsuario":miFormularioUsuario})#

def deportes(request):

      if request.method == 'POST':

            miFormularioDeporte = comentarioFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormularioDeporte)

            if miFormularioDeporte.is_valid:   #Si pasó la validación de Django

                  informacion = miFormularioDeporte.cleaned_data

                  deporte = Deportes (nombre=informacion['Usuario'], categoria=informacion['Categoria'], comentario=informacion['Comentario']) 

                  deporte.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormularioDeporte= comentarioFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/deportes.html", {"miFormularioDeporte":miFormularioDeporte})


def politica(request):
      if request.method == 'POST':

            miFormularioPolitica = comentarioFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormularioPolitica)

            if miFormularioPolitica.is_valid:   #Si pasó la validación de Django

                  informacion = miFormularioPolitica.cleaned_data

                  politica = Politica (nombre=informacion['Usuario'], categoria=informacion['Categoria'], comentario=informacion['Comentario']) 

                  politica.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormularioPolitica= comentarioFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/politica.html", {"miFormularioPolitica":miFormularioPolitica})


def arte(request):

      if request.method == 'POST':

            miFormularioArte = comentarioFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormularioArte)

            if miFormularioArte.is_valid:   #Si pasó la validación de Django

                  informacion = miFormularioArte.cleaned_data

                  arte = Arte (nombre=informacion['Usuario'], categoria=informacion['Categoria'], comentario=informacion['Comentario']) 

                  arte.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormularioArte= comentarioFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/arte.html", {"miFormularioArte":miFormularioArte})

def busquedaComentarioDeporte(request):
      return render(request,"AppCoder/deportes.html")

def buscarDeporte(request):
      
      if request.GET["nombre"]:
            nombre=request.GET['nombre']
            comentario = Deportes.objects.filter(nombre__icontains=nombre)
            return render(request,"AppCoder/deportes.html", {"comentario":comentario, "nombre":nombre})
      else:
            respuesta= "No enviaste datos"
      return HttpResponse(respuesta)

def busquedaComentarioArte(request):
      return render(request,"AppCoder/arte.html")

def buscarArte(request):
      
      if request.GET["nombre"]:
            nombre=request.GET['nombre']
            comentario = Deportes.objects.filter(nombre__icontains=nombre)
            return render(request,"AppCoder/arte.html", {"comentario":comentario, "nombre":nombre})
      else:
            respuesta= "No enviaste datos"
      return HttpResponse(respuesta)

def busquedaComentarioPolitica(request):
      return render(request,"AppCoder/deportes.html")

def buscarPolitica(request):
      
      if request.GET["nombre"]:
            nombre=request.GET['nombre']
            comentario = Deportes.objects.filter(nombre__icontains=nombre)
            return render(request,"AppCoder/politica.html", {"comentario":comentario, "nombre":nombre})
      else:
            respuesta= "No enviaste datos"
      return HttpResponse(respuesta)



@login_required
def editarPerfil(request):
      usuario = request.user
      if request.method == 'POST':
            miFormulario = UserEditForm(request.POST)
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data

                  usuario.email = informacion['email']
                  usuario.password1 = informacion['password1']
                  usuario.password2 = informacion['password2']
                  usuario.last_name = informacion['last_name']
                  usuario.first_name = informacion['first_name']

                  usuario.save()

            return render(request, "AppCoder/inicio.html")

      else:
            miFormulario = UserEditForm(initial={'email': usuario.email})
            
      return render(request, "AppCoder/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})
