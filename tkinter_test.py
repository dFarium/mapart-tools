import tkinter as tk
from tkinter import filedialog

# Función para abrir el cuadro de diálogo de selección de archivos
def seleccionar_archivo():
    archivo = filedialog.askopenfilename(title="Seleccionar archivo")
    if archivo:
        etiqueta.config(text=archivo)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Seleccionar archivo")

# Crear un botón para abrir el cuadro de diálogo de selección de archivos
boton = tk.Button(ventana, text="Seleccionar archivo", command=seleccionar_archivo)
boton.pack(pady=10)

# Crear una etiqueta para mostrar la ruta del archivo seleccionado
etiqueta = tk.Label(ventana, text="No se ha seleccionado ningún archivo")
etiqueta.pack(pady=10)

# Iniciar el bucle principal de la ventana
ventana.mainloop()
