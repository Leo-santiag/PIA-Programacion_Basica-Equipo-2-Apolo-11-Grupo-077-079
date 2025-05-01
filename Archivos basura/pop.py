import pandas as pd

def transformar_columna_tipo(nombre_archivo_entrada, nombre_archivo_salida):
    # Cargar el archivo CSV
    df = pd.read_csv(nombre_archivo_entrada)

    # Convertir la columna 'Tipo' de lista a cadena de texto
    df['Tipo'] = df['Tipo'].apply(lambda x: ', '.join(eval(x)) if isinstance(x, str) else x)

    # Guardar el nuevo archivo CSV
    df.to_csv(nombre_archivo_salida, index=False)
    print(f"Archivo transformado guardado como: {nombre_archivo_salida}")

# Ejemplo de uso
transformar_columna_tipo('archivo_ordenado.csv', 'archivo_transformado.csv')
