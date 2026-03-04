import json
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from api.models import Region, PokedexEntry 

class Command(BaseCommand):
    help = 'Carga la Pokedex con tipos, formas Shiny y corrige el error de instancias de evolución'

    def handle(self, *args, **kwargs):
        self.stdout.write("Leyendo tu archivo pokedex.json...")
        ruta_archivo = os.path.join(settings.BASE_DIR, 'pokedex.json')

        if not os.path.exists(ruta_archivo):
            self.stdout.write(self.style.ERROR('No encontré el archivo pokedex.json'))
            return

        region, _ = Region.objects.get_or_create(nombre="Kanto")

        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            datos_diccionario = json.load(archivo)
            
            # Lista para conectar las evoluciones después de que todos existan
            evoluciones_pendientes = []
            
            # --- PRIMERA PASADA: CREAR O ACTUALIZAR DATOS BÁSICOS ---
            self.stdout.write("Creando registros de Pokémon...")
            for id_texto, datos in datos_diccionario.items():
                numero = int(id_texto)
                
                # Extraer tipos
                tipos = datos.get('type', [])
                tipo_pri = tipos[0] if len(tipos) > 0 else "Normal"
                tipo_sec = tipos[1] if len(tipos) > 1 else None
                
                # Lógica de rutas (usando tu función de media url)
                def sprite_to_media_url(ruta):
                    if not ruta: return None
                    partes = ruta.replace('\\', '/').split('/')
                    rel = '/'.join(partes[partes.index('pokemon'):]) if 'pokemon' in partes else '/'.join(partes[-2:])
                    media_prefix = settings.MEDIA_URL.rstrip('/')
                    host = 'http://127.0.0.1:8000' if getattr(settings, 'DEBUG', False) else ''
                    return f"{host}{media_prefix}/{rel}"

                ruta_normal = datos['sprites'][0]
                ruta_shiny = datos['sprites'][1] if len(datos.get('sprites', [])) > 1 else None

                # CREAR/ACTUALIZAR (Sin asignar la evolución todavía para evitar el ValueError)
                obj, created = PokedexEntry.objects.update_or_create(
                    numero=numero,
                    defaults={
                        'nombre': datos['name'],
                        'tipo_principal': tipo_pri,
                        'tipo_secundario': tipo_sec,
                        'region': region,
                        'sprite_url': sprite_to_media_url(ruta_normal),
                        'sprite_shiny_url': sprite_to_media_url(ruta_shiny),
                        'nivel_evolucion': datos.get('evolution_level')
                    }
                )

                # Guardamos la relación para la segunda pasada
                siguiente = datos.get('next_evolution')
                if siguiente:
                    evoluciones_pendientes.append({
                        'origen': numero,
                        'destino': int(siguiente)
                    })

                status = "Nuevo" if created else "Actualizado"
                self.stdout.write(f"{status}: #{numero} {datos['name']}")

            # --- SEGUNDA PASADA: CONECTAR EVOLUCIONES (Ahora que todos existen) ---
            self.stdout.write("🔗 Conectando líneas evolutivas...")
            for relacion in evoluciones_pendientes:
                try:
                    poke_origen = PokedexEntry.objects.get(numero=relacion['origen'])
                    # Buscamos la INSTANCIA del objeto destino
                    poke_destino = PokedexEntry.objects.get(numero=relacion['destino'])
                    
                    # ASIGNAMOS EL OBJETO, NO EL ID
                    poke_origen.evolucion_siguiente = poke_destino
                    poke_origen.save()
                except PokedexEntry.DoesNotExist:
                    self.stdout.write(self.style.WARNING(f"No se pudo conectar #{relacion['origen']} con #{relacion['destino']}"))

        self.stdout.write(self.style.SUCCESS('¡Pokedex cargada exitosamente!'))