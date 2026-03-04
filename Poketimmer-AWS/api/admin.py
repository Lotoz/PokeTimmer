from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Usuario, Region, PokedexEntry, PokemonUsuario, Tarea

admin.site.register(Usuario)
admin.site.register(Region)
admin.site.register(PokedexEntry)
admin.site.register(PokemonUsuario)
admin.site.register(Tarea)