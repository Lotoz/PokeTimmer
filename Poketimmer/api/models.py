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
    pomo_tiempo_descanso = models.IntegerField(default=5) # Minutos
    pomo_tiempo_descanso_largo = models.IntegerField(default=30) # Minutos
    pomo_ciclos = models.IntegerField(default=3) # Cantidad de ciclos antes del descanso largo

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
    piedra_eterna = models.BooleanField(default=False) # Evita que el Pokémon evolucione
    def __str__(self):
        return f"{self.apodo or self.especie.nombre} de {self.entrenador.username}"
    #Para subir de nivel, se llama cada vez que el usuario gana experiencia (Ej: Completa tareas)
    def ganar_experiencia(self, cantidad):
        self.experiencia += cantidad
        subio_nivel = False
        
        # Lógica de nivel (Ej: Cada 100 de exp = 1 nivel, máximo 100)
        while self.experiencia >= 100 and self.nivel < 100:
            self.nivel += 1
            self.experiencia -= 100
            subio_nivel = True
        
        # Limitar experiencia si alcanzó nivel 100
        if self.nivel >= 100:
            self.experiencia = 0
            
        if subio_nivel:
            self.comprobar_evolucion()
            
        self.save()

    def comprobar_evolucion(self):
        # No evoluciona si tiene Piedra Eterna
        if self.piedra_eterna:
            return
        
        #  Verificamos si la especie actual TIENE una evolución configurada
        # verificamos si TIENE un nivel de evolución asignado
        #  Verificamos si el nivel actual del Pokémon alcanzó o superó esa meta
        if (self.especie.evolucion_siguiente and 
            self.especie.nivel_evolucion and 
            self.nivel >= self.especie.nivel_evolucion):
            
            # ¡Evolución! Cambiamos la especie a la nueva
            self.especie = self.especie.evolucion_siguiente
    
    def calcular_nivel_inicial(self):
        """Calcula el nivel inicial basado en la cadena evolutiva.
        Si el Pokémon capturado es una evolución posterior, inicia en el 
        nivel requerido para evolucionarlo, sino inicia en nivel 1.
        """
        # Verificar qué evoluciones preceden a esta especie
        pre_evoluciones = list(self.especie.pre_evolucion.all())
        
        # Si tiene pre-evoluciones, empezar en el nivel de evolución de la especie
        if pre_evoluciones:
            # Consideramos el nivel de evolución de la especie actual
            # Ya que sería el nivel requerido para hacerlo evolucionar desde su forma anterior
            if self.especie.nivel_evolucion:
                return self.especie.nivel_evolucion
        
        return 1

# TAREAS (Productividad)
class Tarea(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='tareas')
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo