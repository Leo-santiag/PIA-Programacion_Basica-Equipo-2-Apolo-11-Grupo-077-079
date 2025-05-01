import pandas as pd
import requests
import time

# Carga tu CSV original
df = pd.read_csv("archivo_ordenado.csv")

# Función para obtener la URL del sprite oficial desde la PokéAPI
def obtener_url_oficial(poke_id):
    url_api = f"https://pokeapi.co/api/v2/pokemon/{poke_id}"
    try:
        response = requests.get(url_api, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data['sprites']['front_default']
    except Exception as e:
        print(f"Error al obtener el ID {poke_id}: {e}")
    return None

# Solo para los Pokémon que no tienen URL de imagen
faltantes = df['URL imagen'].isnull()

# Aplicamos la función para obtener la URL oficial
df.loc[faltantes, 'URL imagen'] = df.loc[faltantes, 'ID'].apply(obtener_url_oficial)

# Guardar los cambios
df.to_csv("pokemon_con_urls_actualizadas.csv", index=False)

print("✅ URLs actualizadas y archivo guardado.")
