#Extracción de Datos
import requests
import pandas as pd
import re
Tipos = [
    "steel", "water", "bug", "dragon", "electric", "ghost",
    "fire", "fairy", "ice", "fighting", "normal", "grass",
    "psychic", "rock", "dark", "ground", "poison", "flying"
]
def validar_nombre_pokemon(nombre):
    # expresion regular para validar nombres de pokemon solo letras y numeros
    # valida el nombre comprueba si la cadena nombre contiene solo letras y numeros y si cumple con la estructura definida por la expresion regular
    patron = re.compile(r'^[a-zA-Z0-9-]+$')
    # retorno devuelve true si la cadena nombre coincide con la expresion regular y false si no coincide
    return patron.match(nombre) is not None
def obtener_pokemones_por_tipo(tipo):
    tipo = tipo.lower()
#Realizar consultas a la API seleccionada para obtener los datos en formato JSON. 
#Validar las consultas utilizando expresiones regulares para garantizar la precisión de las entradas y asegurar que los datos recuperados sean relevantes. 
    # no se necesita validar los tipos ya que han sido tomado correctamente de la lista Tipos
    #YA SE VALIDA EN EL MODULO API_Conect del anterior entregable
    url = f"https://pokeapi.co/api/v2/type/{tipo}"
    respuesta = requests.get(url)
    
    if respuesta.status_code != 200:
        raise Exception(f"Error al obtener los datos del tipo {tipo}")
    #da la lista de los pokemones 
    lista_pokemones = respuesta.json()["pokemon"]
    # se crea una list vacia que almacenara los datos de cada uno de los pokemones para luego ser ecportada a un csv
    datos_pokemones = []
    #para cada pokemon en la lista que se toma por tipo
    for entrada in lista_pokemones:

        nombre = entrada["pokemon"]["name"]
        if not validar_nombre_pokemon(nombre):
            print("nombre de pokemon invalido por favor ingrese un nombre valido")
            return None
        #no se necesita validacion ya que los nombres has sido sacados de la propia lista de la api 
        #YA SE VALIDA EN EL MODULO API_Conect del anterior entregable
        data = requests.get(f"https://pokeapi.co/api/v2/pokemon/{nombre}").json()
        #creacion de nuestro df con pandas
#Analizar los datos obtenidos del JSON para identificar y eliminar información irrelevante o innecesaria. 
        datos_pokemones.append({
            "ID": data["id"],
            "Nombre": data["name"],
            #Corrección de formatos al usar el .join
            "Tipo": ", ".join([tipo_info["type"]["name"] for tipo_info in data["types"]]),
            "HP":data["stats"][0]["base_stat"],
            "Ataque": data["stats"][1]["base_stat"],
            "Defensa": data["stats"][2]["base_stat"],
            "Ataque Especial": data["stats"][3]["base_stat"],
            "Defensa Especial": data["stats"][4]["base_stat"],
            "Velocidad": data["stats"][5]["base_stat"],
            "Altura": data["height"],
            "Peso": data["weight"],
            #Resolución de inconsistencias o valores erróneos en los datos. 
            #omitimos estos porque son muchos datos inecesarios y son muchos 
            #"Habilidades": ", ".join([habilidad["ability"]["name"] for habilidad in data["abilities"]]),
            "Experiencia Base": data["base_experience"],
            #"Movimientos": ", ".join([movimiento["move"]["name"] for movimiento in data["moves"]]),  # Todos los movimientos
            "URL imagen": data["sprites"]["front_default"],
            
        })
    #nos regresa el df 
    return pd.DataFrame(datos_pokemones)
#se crea una funcion para exporar a csv el df creado 
#funcionalidad extra agrega los datos sin rescribirlos por lo que se acumulara todos los datos de todos lo pokemones en un solo csv
def exportar_a_csv(df, nombre_archivo):
    df.to_csv(nombre_archivo, index=False, mode='a', header=not pd.io.common.file_exists(nombre_archivo))
#se especifica el nombre del archivo y se crea si no esta creado
nombre_archivo = "pokemones.csv"

#en un bucle for preparamos toda la extraccion 
df_general = pd.DataFrame()
for tipo in Tipos:
    df = obtener_pokemones_por_tipo(tipo)
    df_general = pd.concat([df_general, df], ignore_index=True)
#Almacenamiento de Datos: 
#Guardar los datos procesados y estructurados en archivos de texto (por ejemplo, con formato .txt o .csv) para que puedan ser utilizados de manera consistente en las siguientes fases del proyecto. 
exportar_a_csv(df_general, nombre_archivo)