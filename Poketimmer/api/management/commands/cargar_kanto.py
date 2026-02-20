import json
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from api.models import Region, PokedexEntry 

class Command(BaseCommand):
    help = 'Carga la Pokedex desde tu archivo JSON personalizado, incluyendo evoluciones y múltiples tipos'

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
            self.stdout.write("Creando registros de Pokémon con tipos...")
            for id_texto, datos in datos_diccionario.items():
                numero = int(id_texto)
                nombre = datos['name']
                
                # --- CORRECCIÓN DE TIPOS ---
                # Extraemos el array de tipos
                lista_tipos = datos.get('type', [])
                
                # El primero siempre existe según tu JSON
                tipo_pri = lista_tipos[0] if len(lista_tipos) > 0 else "Normal"
                
                # El segundo solo si el array tiene longitud mayor a 1
                tipo_sec = lista_tipos[1] if len(lista_tipos) > 1 else None
                
                # Manejo de sprites normal y shiny (mapear a /media/pokemon/...)
                ruta_normal = datos['sprites'][0]
                ruta_shiny = datos['sprites'][1] if len(datos.get('sprites', [])) > 1 else None

                # Convertir la ruta del JSON (p. ej. "public/pokemon/normal/ivysaur.png")
                # a la ruta servida por Django durante desarrollo: /media/pokemon/normal/ivysaur.png
                def sprite_to_media_url(ruta):
                    if not ruta:
                        return None
                    partes = ruta.replace('\\', '/').split('/')
                    # Intentamos localizar la subruta 'pokemon' en la ruta original
                    if 'pokemon' in partes:
                        idx = partes.index('pokemon')
                        rel = '/'.join(partes[idx:])  # ej: pokemon/normal/ivysaur.png
                    else:
                        # fallback: últimos dos segmentos (normal/ivysaur.png)
                        rel = '/'.join(partes[-2:])
                    # Aseguramos que MEDIA_URL no duplique slashes
                    media_prefix = settings.MEDIA_URL.rstrip('/')
                    # En desarrollo servimos los medios desde el backend en http://127.0.0.1:8000
                    if getattr(settings, 'DEBUG', False):
                        host = 'http://127.0.0.1:8000'
                    else:
                        host = ''
                    return f"{host}{media_prefix}/{rel}"

                ruta_web_normal = sprite_to_media_url(ruta_normal)
                ruta_web_shiny = sprite_to_media_url(ruta_shiny) if ruta_shiny else None
                # Nivel de evolución
                nivel_evo = datos.get('evolution_level')

                obj, created =PokedexEntry.objects.update_or_create(
                        numero=int(id_texto),
                    defaults={
                        'nombre': nombre,
                        'tipo_principal': tipo_pri,
                        'tipo_secundario': tipo_sec, # Nuevo campo
                        'region': region,
                        'sprite_url': ruta_web_normal,
                        'sprite_shiny_url': ruta_web_shiny,
                        'nivel_evolucion': nivel_evo
                    }
                )

                if created:
                    self.stdout.write(f"Nuevo: #{numero} {nombre} [{tipo_pri}{'/' + tipo_sec if tipo_sec else ''}]")
                else:
                    self.stdout.write(f"Actualizado: #{numero} {nombre}")

                # Guardamos la intención de evolución
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
                    
                    poke_origen.evolucion_siguiente = poke_destino
                    poke_origen.save()
                    
                except PokedexEntry.DoesNotExist:
                    self.stdout.write(self.style.WARNING(
                        f"ERROR: No se pudo enlazar #{relacion['origen']} con #{relacion['destino']}."
                    ))

        self.stdout.write(self.style.SUCCESS('¡Datos, tipos y evoluciones cargados exitosamente!'))