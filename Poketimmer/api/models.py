from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

#  USUARIO PERSONALIZADO
class Usuario(AbstractUser):
    # Campos extra además de usuario/contraseña
    foto_perfil = models.ImageField(upload_to='perfiles/', null=True, blank=True)
    tema_app = models.CharField(max_length=50, default='light') 
    
    # Configuración Pomodoro
    pomo_tiempo_trabajo = models.IntegerField(default=25) # Minutos
    pomo_tiempo_descanso = models.IntegerField(default=5)

# SISTEMA POKEMON (Pokedex)
class Region(models.Model):
    nombre = models.CharField(max_length=50) # Ej: Kanto
    
    def __str__(self):
        return self.nombre

class PokedexEntry(models.Model):
    numero = models.IntegerField(unique=True) 
    nombre = models.CharField(max_length=100)
    tipo_principal = models.CharField(max_length=50)
    tipo_secundario = models.CharField(max_length=50, null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    sprite_url = models.CharField(max_length=255, blank=True)
    sprite_shiny_url = models.CharField(max_length=255, blank=True, null=True) 
    # NUEVOS CAMPOS PARA LA EVOLUCIÓN
    evolucion_siguiente = models.ForeignKey(
        'self', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='pre_evolucion'
    )
    nivel_evolucion = models.IntegerField(null=True, blank=True) # Ej: 16

    def __str__(self):
        return f"#{self.numero} {self.nombre}"

# EL PC DEL USUARIO 
class PokemonUsuario(models.Model):
    entrenador = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='mis_pokemon')
    especie = models.ForeignKey(PokedexEntry, on_delete=models.CASCADE)
    apodo = models.CharField(max_length=100, blank=True, null=True)
    nivel = models.IntegerField(default=1)
    experiencia = models.IntegerField(default=0)
    en_equipo = models.BooleanField(default=False) # ¿Está en el dashboard?
    fecha_captura = models.DateTimeField(auto_now_add=True)
    es_shiny = models.BooleanField(default=False) # Para saber si el pokemon capturado es shiny o no
    def __str__(self):
        return f"{self.apodo or self.especie.nombre} de {self.entrenador.username}"
    #Para subir de nivel, se llama cada vez que el usuario gana experiencia (Ej: Completa tareas)
    def ganar_experiencia(self, cantidad):
        self.experiencia += cantidad
        subio_nivel = False
        
        # Lógica de nivel (Ej: Cada 100 de exp = 1 nivel)
        while self.experiencia >= 100:
            self.nivel += 1
            self.experiencia -= 100
            subio_nivel = True
            
        if subio_nivel:
            self.comprobar_evolucion()
            
        self.save()

    def comprobar_evolucion(self):
        #  Verificamos si la especie actual TIENE una evolución configurada
        # verificamos si TIENE un nivel de evolución asignado
        #  Verificamos si el nivel actual del Pokémon alcanzó o superó esa meta
        if (self.especie.evolucion_siguiente and 
            self.especie.nivel_evolucion and 
            self.nivel >= self.especie.nivel_evolucion):
            
            # ¡Evolución! Cambiamos la especie a la nueva
            self.especie = self.especie.evolucion_siguiente

# TAREAS (Productividad)
class Tarea(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='tareas')
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo