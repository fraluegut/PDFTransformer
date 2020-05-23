from tkinter import *
from tkinter import messagebox
from tkinter import filedialog, Entry
from main import extract_information
import tkinter as tk
window = Tk()
from PyPDF2 import PdfFileReader, PdfFileMerger, PdfFileWriter
window.title("PDF to A5 Printable Book")



window.filename = None
def clicked():
    window.filename = filedialog.askopenfilename(initialdir="/home/fraluegut/Descargas", title="Select file", filetypes=(("all files", "*.*"), ("jpeg files", "*.jpg")))

    with open(window.filename, 'rb') as f:
        pdf = PdfFileReader(f)
        result = pdf.getNumPages()
    numero_paginas_result.configure(text=result)
    print(window.filename)

    return window.filename

# Display

btn = Button(window, text="Seleccionar documento", command=clicked) # Botón de selección de archivo
btn.grid(column=1, row=0)

nombre_salida = tk.Entry(window) # Nombre de salida
nombre_salida.grid(column=1, row=1)

ubicacion_salida = Button(window, text="Ubicación de salida", command=clicked) # Botón de Ubicación de salida
ubicacion_salida.grid(column=1, row=2)

numero_paginas = Label(window, text="Número de páginas del archivo: ") # Número de páginas del archivo
numero_paginas.grid(column=1, row=3)
numero_paginas_result = Label(window, text="")
numero_paginas_result.grid(column=1, row=4)

numero_folios = Label(window, text="Número de folios necesarios: ") # Número de folios necesarios
numero_folios.grid(column=1, row=5)
numero_paginas_result = Label(window, text="")
numero_paginas_result.grid(column=1, row=6)

if window.filename is not None:
    a = window.filename
    print(a)


window.geometry('350x200')
window.mainloop()