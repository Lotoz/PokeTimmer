import requests
import json
import time

def generar_pokedex(limite=150):
    pokedex_final = {}
    
    for i in range(1, limite + 1):
        print(f"Obteniendo datos de #{i}...")
        
        # 1. Obtener datos básicos (Tipos)
        url_base = f"https://pokeapi.co/api/v2/pokemon/{i}"
        res_base = requests.get(url_base).json()
        
        nombre_capitalizado = res_base['name'].capitalize()
        tipos = [t['type']['name'].capitalize() for t in res_base['types']]
        
        # 2. Obtener datos de especie (Descripción y URL de evolución)
        url_especie = f"https://pokeapi.co/api/v2/pokemon-species/{i}"
        res_especie = requests.get(url_especie).json()
        
        # Buscar la primera descripción en inglés
        descripcion = "Descripción no disponible."
        for entry in res_especie['flavor_text_entries']:
            if entry['language']['name'] == 'en':
                # Limpiar saltos de línea raros de la PokeAPI
                descripcion = entry['flavor_text'].replace('\n', ' ').replace('\f', ' ')
                break
                
        # 3. Lógica de Evolución (Navegar por la cadena evolutiva)
        url_evolucion = res_especie['evolution_chain']['url']
        res_evolucion = requests.get(url_evolucion).json()
        
        # Función recursiva para buscar al pokemon actual en el árbol de evoluciones
        def buscar_nodo(nodo, nombre):
            if nodo['species']['name'] == nombre:
                return nodo
            for hijo in nodo['evolves_to']:
                resultado = buscar_nodo(hijo, nombre)
                if resultado:
                    return resultado
            return None

        nodo_actual = buscar_nodo(res_evolucion['chain'], res_base['name'])
        
        next_evolution = None
        evolution_level = None
        
        # Si tiene evolución, extraemos los datos
        if nodo_actual and len(nodo_actual['evolves_to']) > 0:
            siguiente_nodo = nodo_actual['evolves_to'][0]
            
            # Extraer ID del siguiente Pokemon desde su URL
            url_siguiente_especie = siguiente_nodo['species']['url']
            siguiente_id = url_siguiente_especie.rstrip('/').split('/')[-1]
            next_evolution = str(siguiente_id).zfill(4)
            
            # Obtener el nivel de evolución si existe
            detalles = siguiente_nodo['evolution_details']
            if detalles and len(detalles) > 0:
                evolution_level = detalles[0].get('min_level')
        
        # 4. Construir el objeto con tu formato exacto
        id_str = str(i).zfill(4)
        pokedex_final[id_str] = {
            "name": nombre_capitalizado,
            "type": tipos,
            "description": descripcion,
            "Pokédex entries": [
                {
                    "game": "Game(Actualiza el script para asignar el juego correcto)",
                    "entry": descripcion
                }
            ],
            "sprites": [
                f"Poketimmer/api/templates/pokemon/{nombre_capitalizado}Sprite.png",
                f"Poketimmer/api/templates/pokemon/{nombre_capitalizado}ShinySprite.png"
            ],
            "next_evolution": next_evolution,
            "evolution_level": evolution_level
        }
        
        # Pausa para no saturar la API pública
        time.sleep(0.5)

    # 5. Guardar en un archivo JSON
    with open('pokedex.json', 'w', encoding='utf-8') as f:
        json.dump(pokedex_final, f, indent=4, ensure_ascii=False)
        
    print(f"\n¡Éxito! Se ha generado el archivo 'pokedex.json' con {limite} Pokémon.")

# Ejecutar el script
if __name__ == "__main__":
    generar_pokedex(70)