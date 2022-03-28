from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.forms import comentarioFormulario, usuarioFormulario
from AppCoder.models import Usuario, Politica, Deportes, Arte


# Create your views here.


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

      return render(request, "AppCoder/usuarios.html", {"miFormularioUsuario":miFormularioUsuario})

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

def busquedaComentario(request):
      return render(request,"AppCoder/deportes.html")

def buscar(request):
      
      if request.GET["nombre"]:
            nombre=request.GET['nombre']
            comentario = Deportes.objects.filter(nombre__icontains=nombre)
            return render(request,"AppCoder/deportes.html", {"comentario":comentario, "nombre":nombre})
      else:
            respuesta= "No enviaste datos"
      return HttpResponse(respuesta)
