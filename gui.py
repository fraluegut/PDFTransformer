import webbrowser
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog, Entry, Checkbutton, Radiobutton
import tkinter.filedialog as filedialog
import tkinter as tk
from PyPDF2 import PdfFileReader, PdfFileMerger, PdfFileWriter
import math
import numpy as np
import webbrowser as wb
from os import remove
import os
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
    global numero_folios_reales
    global input_path
    input_path = tk.filedialog.askopenfilename()
    input_entry.delete(1, tk.END)  # Remove current text in entry
    input_entry.insert(0, input_path)  # Insert the 'path'
    with open(input_path, 'rb') as f:
        pdf = PdfFileReader(f)
        numero_pg = pdf.getNumPages()
    numero_paginas_result.configure(text='Número de páginas: ' + str(numero_pg))
    numero_folios_result.configure(text='Número de folios: ' + str(math.ceil(numero_pg/4)))
    numero_folios_reales = math.ceil(numero_pg / 4)
    print(input_entry)
    print(input_path)
    return numero_folios_reales, input_path

def output():
    global path
    path = filedialog.askdirectory()
    output_entry.delete(1, tk.END)  # Remove current text in entry
    output_entry.insert(0, str(path))  # Insert the 'path'
    return path

def split(path, name_of_split):
    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        output = f'{name_of_split}{page}.pdf'
        with open(output, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

def print_selection():
    l.config(text='Ha seleccionado  ' + var.get())


def establecer_n_libritos():
    #with open(input_path, 'rb') as f:
        #pdf = PdfFileReader(f)
        #numero_pg = pdf.getNumPages()
    numero_pg = 100
    print(numero_pg)
    numero_libritos = int(numero_pg/20)
    print(numero_libritos)
    pagina = 0
    for i in range(1, numero_libritos+1):
        libro = "librito_%s" %(i)
        print(libro)
        librito = range(pagina+1, pagina+20)
        print(librito)
        pagina= pagina + 20


establecer_n_libritos()
def procesar():
    print(input_path)

    split(str(input_path), str(nombre_salida_entry.get())+"_")

    # Matrix con num min de carillas que es el mínimo común múltiplo del número de páginas
    matrix = np.arange(numero_folios_reales * 4).reshape((numero_folios_reales, 4))

    matrix[numero_folios_reales - 1, 2] = (numero_folios_reales * 4) / 2
    matrix[numero_folios_reales - 1, 1] = matrix[numero_folios_reales - 1, 2] - 1
    matrix[numero_folios_reales - 1, 3] = matrix[numero_folios_reales - 1, 2] + 1
    matrix[numero_folios_reales - 1, 0] = matrix[numero_folios_reales - 1, 3] + 1

    for i in range(int(numero_folios_reales) - 2, -1, -1):
        # print(i)
        matrix[i, 0] = matrix[i + 1, 0] + 2
        matrix[i, 1] = matrix[i + 1, 1] - 2
        matrix[i, 2] = matrix[i + 1, 2] - 2
        matrix[i, 3] = matrix[i + 1, 3] + 2

    Pdfs_cara_A = []

    for i in range(0, numero_folios_reales):

        if ("%s_%s.pdf" % (str(nombre_salida_entry.get()), (matrix[i, 0] - 1))) != None:
            Pdfs_cara_A.append("%s_%s.pdf" % (str(nombre_salida_entry.get()), (matrix[i, 0] - 1)))
        else:
            Pdfs_cara_A.append("pdf_blanco.pdf")

        if ("%s_%s.pdf" % (str(nombre_salida_entry.get()), (matrix[i, 1] - 1))) != None:
            Pdfs_cara_A.append("%s_%s.pdf" % (str(nombre_salida_entry.get()), (matrix[i, 1] - 1)))
        else:
            Pdfs_cara_A.append("pdf_blanco.pdf")

    Pdfs_cara_B = []

    for i in range(0, numero_folios_reales):

        if ("%s_%s.pdf" % (str(nombre_salida_entry.get()), (matrix[i, 2] - 1))) != None:
            Pdfs_cara_B.append("%s_%s.pdf" % (str(nombre_salida_entry.get()), (matrix[i, 2] - 1)))
        else:
            Pdfs_cara_B.append("pdf_blanco.pdf")

        if ("%s_%s.pdf" % (str(nombre_salida_entry.get()), (matrix[i, 3] - 1))) != None:
            Pdfs_cara_B.append("%s_%s.pdf" % (str(nombre_salida_entry.get()), (matrix[i, 3] - 1)))
        else:
            Pdfs_cara_B.append("pdf_blanco.pdf")


    merger = PdfFileMerger()

    for pdf in Pdfs_cara_A:
        try:
            merger.append(pdf)
        except FileNotFoundError:
            merger.append("pdf_blanco.pdf")
    for pdf in Pdfs_cara_B:
        try:
            merger.append(pdf)
        except FileNotFoundError:
            merger.append("pdf_blanco.pdf")
    # Juntamos muy junticos los pdfs resultantes y le damos el nombre que indicó el usuario en nombre_salida_entry a través de un get().
    merger.write(nombre_salida_entry.get())
    merger.close()
    url_salida = str(output_entry.get()) + "/" + nombre_salida_entry.get()
    # Abre el documento resultante
    wb.open_new(url_salida)
    for pdf in Pdfs_cara_A:
        try:
            remove("%s/%s" % (path, pdf))
        except:
            continue
    for pdf in Pdfs_cara_B:
        try:
            remove("%s/%s" % (path, pdf))
        except:
            continue
    #os.system(f'start {os.path.realpath(url_salida)}')
    directorio = path.replace("/", "//")
    print(directorio)
    webbrowser.open(directorio)
##################### Display ######################################



# Frame
frame_base = tk.Frame(window)
frame_base.pack(side=tk.TOP)

# Texto Ubicación del archivo original:
input_path = tk.Label(frame_base, text="Ubicación del archivo original:")
input_path.pack(pady=5)

# Hueco para ruta del archivo original:
input_entry = tk.Entry(frame_base, text="", width=40)
input_entry.pack(pady=5)

# Botón Seleccionar ubicación:
browse1 = tk.Button(frame_base, text="Seleccionar ubicación", command=input)
browse1.pack(pady=5)

# Texto Ubicación de la carpeta de salida:
output_path = tk.Label(frame_base, text="Ubicación de la carpeta de salida:")
output_path.pack(pady=5)

# Hueco para ruta de la ubicación de salida:
output_entry = tk.Entry(frame_base, text="", width=40)
output_entry.pack(pady=5)

# Botón Seleccionar ubicación de salida
browse2 = tk.Button(frame_base, text="Seleccionar ubicación de salida", command=output)
browse2.pack(pady=5)

# Texto "Nombre salida":
nombre_salida = tk.Label(frame_base, text="Nombre salida:")
nombre_salida.pack(pady=5)

# Hueco para introducir nombre_salida:
nombre_salida_entry = tk.Entry(frame_base, text="", width=40)
nombre_salida_entry.pack(pady=5)

# RadioButton Impresora doble cara/Impresora una cara
var = tk.StringVar()
r1 = tk.Radiobutton(frame_base, text='Impresora doble cara', variable=var, value='impresora doble cara', command=print_selection)
r1.pack()
r2 = tk.Radiobutton(frame_base, text='Impresora una cara', variable=var, value='impresora una cara', command=print_selection)
r2.pack()

# Hueco para la impresora elegida
l = tk.Label(frame_base, bg='white', width=200, text='')
l.pack(pady=5)

# Botón Procesar
browse3 = tk.Button(frame_base, text="Procesar", command=procesar)
browse3.pack(pady=5)

# Texto Resumen
resumen = tk.Label(frame_base, bg='white', width=200, text='Resumen')
resumen.pack(pady=5)

# Texto Número de páginas:
numero_paginas_result = tk.Label(frame_base, bg='white', width=200, text='Número de páginas: ')
numero_paginas_result.pack(pady=5)

# Texto Número de folios:
numero_folios_result = tk.Label(frame_base, bg='white', width=200, text='Número de folios: ')
numero_folios_result.pack(pady=5)


if window.filename is not None:
    a = window.filename


# Dimensiones de la ventana
window.geometry('700x500')
window.mainloop()
