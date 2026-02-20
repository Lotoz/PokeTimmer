import os
import requests
import time

def descargar_de_pokeapi(limite=151):
    # Definir rutas de medios para Django
    base_path = "media/pokemon"
    folders = {
        "normal": f"{base_path}/normal",
        "shiny": f"{base_path}/shiny"
    }

    # Crear carpetas si no existen
    for folder in folders.values():
        os.makedirs(folder, exist_ok=True)

    print(f"🚀 Iniciando descarga de {limite} Pokémon...")

    for i in range(1, limite + 1):
        try:
            # Consultar datos del Pokémon por ID
            response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{i}", timeout=10)
            if response.status_code != 200:
                print(f"❌ Error al obtener datos del ID {i}")
                continue

            data = response.json()
            nombre = data['name']
            
            # Extraer URLs de sprites (oficiales de la PokeAPI)
            url_normal = data['sprites']['front_default']
            url_shiny = data['sprites']['front_shiny']

            # Descargar normal
            if url_normal:
                descargar_imagen(url_normal, f"{folders['normal']}/{nombre}.png")
            
            # Descargar shiny
            if url_shiny:
                descargar_imagen(url_shiny, f"{folders['shiny']}/{nombre}.png")

            # Pausa breve para ser respetuosos con la API
            time.sleep(0.05)

        except Exception as e:
            print(f"⚠️ Error en ID {i}: {e}")

def descargar_imagen(url, ruta_destino):
    try:
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(ruta_destino, 'wb') as f:
                for chunk in r.iter_content(1024):
                    f.write(chunk)
            print(f"✅ Guardado: {ruta_destino}")
    except Exception as e:
        print(f"🔥 Fallo crítico en {url}: {e}")

if __name__ == "__main__":
    descargar_de_pokeapi(151)