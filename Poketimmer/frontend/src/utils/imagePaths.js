/**
 * Convierte una URL de Django a una ruta local de la carpeta public/pokemon
 * @param {string} djangoUrl - URL completa de Django (ej: http://127.0.0.1:8000/media/pokemon/normal/ivysaur.png)
 * @returns {string} Ruta local para servir desde public (ej: /pokemon/normal/ivysaur.png)
 */
export const getLocalPath = (djangoUrl) => {
    if (!djangoUrl) return '';

    // Extrae la parte "/pokemon/..." de la URL de Django
    const parts = djangoUrl.split('/pokemon/');
    return parts.length > 1 ? '/pokemon/' + parts[1] : djangoUrl;
};

/**
 * Obtiene la ruta de imagen normal de un pokemon
 * @param {string} pokemonName - Nombre del pokemon
 * @returns {string} Ruta local de la imagen
 */
export const getNormalImagePath = (pokemonName) => {
    return `/pokemon/normal/${pokemonName.toLowerCase()}.png`;
};

/**
 * Obtiene la ruta de imagen shiny de un pokemon
 * @param {string} pokemonName - Nombre del pokemon
 * @returns {string} Ruta local de la imagen
 */
export const getShinyImagePath = (pokemonName) => {
    return `/pokemon/shiny/${pokemonName.toLowerCase()}.png`;
};

/**
 * Convierte una URL de Django o nombre de pokemon a ruta local
 * Soporta tanto URLs de Django como simples nombres de pokemon
 * @param {string} input - URL de Django o nombre de pokemon
 * @param {string} type - 'normal' o 'shiny' (por defecto 'normal')
 * @returns {string} Ruta local para servir desde public
 */
export const getImagePath = (input, type = 'normal') => {
    if (!input) return '';

    // Si es una URL de Django, extrae solo la parte relativa
    if (input.includes('http') || input.includes('/media/')) {
        return getLocalPath(input);
    }

    // Si es un nombre de pokemon, construye la ruta
    if (type === 'shiny') {
        return getShinyImagePath(input);
    }

    return getNormalImagePath(input);
};
