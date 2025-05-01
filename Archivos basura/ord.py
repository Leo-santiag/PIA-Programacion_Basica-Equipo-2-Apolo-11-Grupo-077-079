import os
import re

def procesar_archivos_txt(carpeta):
    """
    Procesa archivos .txt en una carpeta, extrayendo el tipo de Pokémon desde el nombre del archivo
    y convirtiendo la lista de números en listas de Python, agrupadas en un diccionario.
    
    Parámetro:
        carpeta (str): Ruta de la carpeta que contiene los archivos .txt.
    
    Retorna:
        dict: Diccionario con el tipo de Pokémon como clave y la lista de números como valores.
    """
    pokemon_data = {}

    for archivo in os.listdir(carpeta):
        if archivo.endswith(".txt"):
            # Extraer el tipo de Pokémon desde el nombre del archivo antes del guion
            tipo_pokemon = archivo.split("-")[0].strip()

            # Leer los números de Pokémon desde el archivo
            with open(os.path.join(carpeta, archivo), "r", encoding="utf-8") as f:
                contenido = f.read()

            # Convertir contenido a una lista de números eliminando caracteres no numéricos
            lista_pokemon = [int(num) for num in re.findall(r"\d+", contenido)]

            # Agregar al diccionario
            if tipo_pokemon in pokemon_data:
                pokemon_data[tipo_pokemon].extend(lista_pokemon)
            else:
                pokemon_data[tipo_pokemon] = lista_pokemon

    return pokemon_data

# Definir la variable para almacenar la lista final
ruta_carpeta = "semana 2\pokemonesportipo"
pokemon_lista = procesar_archivos_txt(ruta_carpeta)

# Imprimir la variable para verificar el resultado
print(pokemon_lista)