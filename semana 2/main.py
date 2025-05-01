import tkinter as tk
import csv
# aun no implementamos la busqueda por tipo  
def leer_csv_por_id(id_buscado): 
    nombre_archivo = "archivo_ordenado.csv"
    with open(nombre_archivo, newline='', encoding='utf-8') as archivo_csv:
        lector = csv.DictReader(archivo_csv)
        for fila in lector:
            if fila['ID'] == id_buscado:
                return fila
    return None

def buscar_y_mostrar():
    # Limpiar los resultados anteriores
    for widget in frame_resultados.winfo_children():
        widget.destroy()

    # Obtener el ID ingresado por el usuario
    idIngresado = entradaId.get()
    resultado = leer_csv_por_id(idIngresado)
    
    if resultado:
        #creamos una etiqueta para mostrar cada dato en la fila
        for key, value in resultado.items():
            etiqueta = tk.Label(frame_resultados, text=f"{key.capitalize()}: {value}", bg="#FF0000")
            etiqueta.pack()
    else:
        etiqueta = tk.Label(frame_resultados, text=f"No encontrado ID: {idIngresado}", bg="#FF0000")
        etiqueta.pack()

#parte de tkinter
ventana = tk.Tk()
ventana.title("Buscar en CSV por ID")
ventana.geometry("500x500")
ventana.configure(bg="#FF0000")
#crear frame principal
frameBusqueda = tk.Frame(ventana, bg="#FF0000")
frameBusqueda.pack(pady=10)

labelInstruccion = tk.Label(frameBusqueda, text="Ingrese un ID:", bg="#FF0000")
labelInstruccion.pack(side='left')

entradaId = tk.Entry(frameBusqueda,bg="#FF0000")
entradaId.pack(side='left', padx=5)
boton_buscar = tk.Button(frameBusqueda, text="Buscar", command=buscar_y_mostrar, bg="#FF0000")
boton_buscar.pack(side='left')

frame_resultados = tk.Frame(ventana,bg="#FF0000")
frame_resultados.pack(pady=20)

ventana.mainloop()
