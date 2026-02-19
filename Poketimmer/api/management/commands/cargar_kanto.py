import json
import os
from django.core.management.base import BaseCommand
from django.conf import settings
# Asegúrate de importar tu modelo actualizado
from api.models import Region, PokedexEntry 

class Command(BaseCommand):
    help = 'Carga la Pokedex desde tu archivo JSON personalizado, incluyendo evoluciones'

    def handle(self, *args, **kwargs):
        self.stdout.write("Leyendo tu archivo pokedex.json...")

        ruta_archivo = os.path.join(settings.BASE_DIR, 'pokedex.json')

        if not os.path.exists(ruta_archivo):
            self.stdout.write(self.style.ERROR('No encontré el archivo pokedex.json'))
            return

        # Asegurar Región
        region, _ = Region.objects.get_or_create(nombre="Kanto")

        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            datos_diccionario = json.load(archivo)
            
            # Lista temporal para guardar las relaciones que conectaremos al final
            evoluciones_pendientes = []
            
            # --- PRIMERA PASADA: CREAR LOS POKÉMON ---
            self.stdout.write("Creando registros de Pokémon...")
            for id_texto, datos in datos_diccionario.items():
                numero = int(id_texto)
                nombre = datos['name']
                tipo = datos['type'][0] 
                ruta_original = datos['sprites'][0]
                nombre_archivo = os.path.basename(ruta_original)
                ruta_web = f"/pokemon/{nombre_archivo}"
                
                # Extraemos el nivel de evolución (puede ser None/null)
                nivel_evo = datos.get('evolution_level')

                obj, created = PokedexEntry.objects.update_or_create(
                    numero=numero,
                    defaults={
                        'nombre': nombre,
                        'tipo_principal': tipo,
                        'region': region,
                        'sprite_url': ruta_web,
                        'nivel_evolucion': nivel_evo  # Nuevo campo añadido
                    }
                )

                if created:
                    self.stdout.write(f"Nuevo: #{numero} {nombre}")
                else:
                    self.stdout.write(f"Actualizado: #{numero} {nombre}")

                # Guardamos la intención de evolución para la segunda pasada
                siguiente = datos.get('next_evolution')
                if siguiente:
                    evoluciones_pendientes.append({
                        'origen': numero,
                        'destino': int(siguiente)
                    })

            # --- SEGUNDA PASADA: CONECTAR LAS EVOLUCIONES ---
            self.stdout.write("🔗 Conectando las líneas evolutivas...")
            for relacion in evoluciones_pendientes:
                try:
                    poke_origen = PokedexEntry.objects.get(numero=relacion['origen'])
                    poke_destino = PokedexEntry.objects.get(numero=relacion['destino'])
                    
                    # Enlazamos la clave foránea 'self'
                    poke_origen.evolucion_siguiente = poke_destino
                    poke_origen.save()
                    
                except PokedexEntry.DoesNotExist:
                    self.stdout.write(self.style.WARNING(
                        f"ERROR: No se pudo enlazar #{relacion['origen']} con #{relacion['destino']} porque uno no existe en la BD."
                    ))

        self.stdout.write(self.style.SUCCESS('¡Datos y evoluciones cargados exitosamente!'))