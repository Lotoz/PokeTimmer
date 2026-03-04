import requests
import json
import time

def generar_pokedex(limite=150):
    pokedex_final = {}
    
    for i in range(1, limite + 1):
        print(f"Obteniendo datos de #{i}...")
        
        try:
            # 1. Obtener datos básicos
            url_base = f"https://pokeapi.co/api/v2/pokemon/{i}"
            res_base = requests.get(url_base).json()
            
            nombre_api = res_base['name'] # Nombre original para los archivos (ej: bulbasaur)
            nombre_capitalizado = nombre_api.capitalize()
            tipos = [t['type']['name'].capitalize() for t in res_base['types']]
            
            # 2. Obtener datos de especie (Descripción)
            url_especie = f"https://pokeapi.co/api/v2/pokemon-species/{i}"
            res_especie = requests.get(url_especie).json()
            
            descripcion = "Description not available."
            for entry in res_especie['flavor_text_entries']:
                if entry['language']['name'] == 'en':
                    descripcion = entry['flavor_text'].replace('\n', ' ').replace('\f', ' ')
                    break
                    
            # 3. Lógica de Evolución
            url_evolucion = res_especie['evolution_chain']['url']
            res_evolucion = requests.get(url_evolucion).json()
            
            def buscar_nodo(nodo, nombre):
                if nodo['species']['name'] == nombre:
                    return nodo
                for hijo in nodo['evolves_to']:
                    resultado = buscar_nodo(hijo, nombre)
                    if resultado: return resultado
                return None

            nodo_actual = buscar_nodo(res_evolucion['chain'], nombre_api)
            
            next_evolution = None
            evolution_level = None
            
            if nodo_actual and len(nodo_actual['evolves_to']) > 0:
                siguiente_nodo = nodo_actual['evolves_to'][0]
                url_siguiente_especie = siguiente_nodo['species']['url']
                siguiente_id = url_siguiente_especie.rstrip('/').split('/')[-1]
                next_evolution = str(siguiente_id).zfill(4)
                
                detalles = siguiente_nodo['evolution_details']
                if detalles and len(detalles) > 0:
                    evolution_level = detalles[0].get('min_level')
            
            # 4. Construir el objeto con las rutas a /public/pokemon/
            id_str = str(i).zfill(4)
            pokedex_final[id_str] = {
                "name": nombre_capitalizado,
                "type": tipos,
                "description": descripcion,
                "Pokédex entries": [
                    {
                        "game": "Base Game",
                        "entry": descripcion
                    }
                ],
                "sprites": [
                    f"public/pokemon/normal/{nombre_api}.png", # Ruta Normal
                    f"public/pokemon/shiny/{nombre_api}.png"   # Ruta Shiny
                ],
                "next_evolution": next_evolution,
                "evolution_level": evolution_level
            }
            
            time.sleep(0.3) # Un poco más rápido pero seguro

        except Exception as e:
            print(f"Error procesando #{i}: {e}")

    # 5. Guardar en un archivo JSON
    with open('pokedex.json', 'w', encoding='utf-8') as f:
        json.dump(pokedex_final, f, indent=4, ensure_ascii=False)
        
    print(f"\n¡Éxito! Archivo 'pokedex.json' generado para {limite} Pokémon.")

if __name__ == "__main__":
    generar_pokedex(151) # Generamos los 151 de Kanto