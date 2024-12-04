from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(Autor)
admin.site.register(Livros)
admin.site.register(Editoras)
admin.site.register(Reservas)
admin.site.register(Usuarios)
admin.site.register(Emprestimos)