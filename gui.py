from tkinter import *
from tkinter import messagebox
from tkinter import filedialog, Entry, Checkbutton, Radiobutton
import tkinter.filedialog as filedialog
import tkinter as tk

from PyPDF2 import PdfFileReader, PdfFileMerger, PdfFileWriter
import math

# Creación de la ventana
window = Tk()
window.title("PDF to A5 Printable Book") # Nombre de la ventana

window.filename = None

# Funciones
def clicked():
    window.filename = filedialog.askopenfilename(initialdir="/home/fraluegut/Descargas", title="Select file", filetypes=(("all files", "*.*"), ("jpeg files", "*.jpg")))

    with open(window.filename, 'rb') as f:
        pdf = PdfFileReader(f)
        numero_pg = pdf.getNumPages()
    numero_paginas_result.configure(text='Número de páginas: ' + str(numero_pg))
    numero_folios_result.configure(text='Número de folios: ' + str(math.ceil(numero_pg/4)))


    return window.filename, numero_pg

def input():
    input_path = tk.filedialog.askopenfilename()
    input_entry.delete(1, tk.END)  # Remove current text in entry
    input_entry.insert(0, input_path)  # Insert the 'path'
    with open(input_path, 'rb') as f:
        pdf = PdfFileReader(f)
        numero_pg = pdf.getNumPages()
    numero_paginas_result.configure(text='Número de páginas: ' + str(numero_pg))
    numero_folios_result.configure(text='Número de folios: ' + str(math.ceil(numero_pg/4)))

def output():
    path = filedialog.askdirectory()
    output_entry.delete(1, tk.END)  # Remove current text in entry
    output_entry.insert(0, str(path))  # Insert the 'path'

def print_selection():
    l.config(text='Ha seleccionado  ' + var.get())
def procesar():
    None
# Display
"""
btn = Button(window, text="Seleccionar documento", command=clicked) # Botón de selección de archivo
btn.grid(column=1, row=0)

nombre_salida = tk.Entry(window) # Nombre de salida
nombre_salida.grid(column=1, row=1)
#nombre_salida.place(relx=0.0, rely=0.0, anchor=NW)

ubicacion_salida = Button(window, text="Ubicación de salida", command=clicked) # Botón de Ubicación de salida
ubicacion_salida.grid(column=1, row=2)

numero_paginas = Label(window, text="Número de páginas del archivo: ") # Número de páginas del archivo
numero_paginas.grid(column=1, row=3)
numero_paginas_result = Label(window, text="")
numero_paginas_result.grid(column=1, row=4)

numero_folios = Label(window, text="Número de folios necesarios: ") # Número de folios necesarios
numero_folios.grid(column=1, row=5)
numero_folios_result = Label(window, text="")
numero_folios_result.grid(column=1, row=6)
"""

frame_base = tk.Frame(window)
input_path = tk.Label(frame_base, text="Ubicación del archivo original:")
input_entry = tk.Entry(frame_base, text="", width=40)
browse1 = tk.Button(frame_base, text="Seleccionar ubicación", command=input)
output_path = tk.Label(frame_base, text="Ubicación del archivo de salida:")
output_entry = tk.Entry(frame_base, text="", width=40)
browse2 = tk.Button(frame_base, text="Seleccionar ubicación de salida", command=output)

frame_base.pack(side=tk.TOP)

input_path.pack(pady=5)
input_entry.pack(pady=5)
browse1.pack(pady=5)

output_path.pack(pady=5)
output_entry.pack(pady=5)
browse2.pack(pady=5)

var = tk.StringVar()
r1 = tk.Radiobutton(frame_base, text='Impresora doble cara', variable=var, value='impresora doble cara', command=print_selection)
r1.pack()

r2 = tk.Radiobutton(frame_base, text='Impresora una cara', variable=var, value='impresora una cara', command=print_selection)
r2.pack()

l = tk.Label(frame_base, bg='white', width=200, text='')
l.pack(pady=5)

browse3 = tk.Button(frame_base, text="Procesar", command=procesar)
browse3.pack(pady=5)

resumen = tk.Label(frame_base, bg='white', width=200, text='Resumen')
resumen.pack(pady=5)

numero_paginas_result = tk.Label(frame_base, bg='white', width=200, text='Número de páginas: ')
numero_paginas_result.pack(pady=5)

numero_folios_result = tk.Label(frame_base, bg='white', width=200, text='Número de folios: ')
numero_folios_result.pack(pady=5)


if window.filename is not None:
    a = window.filename



window.geometry('700x500')
window.mainloop()

"""
import tkinter.filedialog as filedialog
import tkinter as tk

master = tk.Tk()

def input():
    input_path = tk.filedialog.askopenfilename()
    input_entry.delete(1, tk.END)  # Remove current text in entry
    input_entry.insert(0, input_path)  # Insert the 'path'


def output():
    path = tk.filedialog.askopenfilename()
    input_entry.delete(1, tk.END)  # Remove current text in entry
    input_entry.insert(0, path)  # Insert the 'path'


top_frame = tk.Frame(master)
bottom_frame = tk.Frame(master)
line = tk.Frame(master, height=1, width=400, bg="grey80", relief='groove')

input_path = tk.Label(top_frame, text="Input File Path:")
input_entry = tk.Entry(top_frame, text="", width=40)
browse1 = tk.Button(top_frame, text="Browse", command=input)

output_path = tk.Label(bottom_frame, text="Output File Path:")
output_entry = tk.Entry(bottom_frame, text="", width=40)
browse2 = tk.Button(bottom_frame, text="Browse", command=output)

begin_button = tk.Button(bottom_frame, text='Begin!')

top_frame.pack(side=tk.TOP)
line.pack(pady=10)
bottom_frame.pack(side=tk.BOTTOM)

input_path.pack(pady=5)
input_entry.pack(pady=5)
browse1.pack(pady=5)

output_path.pack(pady=5)
output_entry.pack(pady=5)
browse2.pack(pady=5)

begin_button.pack(pady=20, fill=tk.X)


master.mainloop()
"""