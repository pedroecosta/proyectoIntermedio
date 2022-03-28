from mailbox import NoSuchMailboxError
from django import forms

class usuarioFormulario(forms.Form):
    Nombre=forms.CharField(max_length=30)
    Apellido=forms.CharField(max_length=30)
    Email=forms.EmailField()
    Contraseña=forms.CharField(max_length=15)

class comentarioFormulario(forms.Form):
    Usuario=forms.CharField(max_length=30)
    Categoria=forms.CharField(max_length=30)
    Comentario=forms.CharField(max_length=120)
