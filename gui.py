# Aplicación para Convertir un pdf cualquiera en un pdf con las páginas ordenadas de tal manera
# que se puedan imprimir a doble cara, con dos páginas por hoja y se creen libritos pequeños que cosidos conformen un libro a encuadernar.


##################### Librerías de la aplicación ######################################
import webbrowser
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import tkinter.filedialog as filedialog
import statistics
import math
import numpy as np
import webbrowser as wb
from os import remove
from docx import Document
from PyPDF2 import PdfFileReader, PdfFileMerger, PdfFileWriter


# Creación de la ventana en Tkinter.
window = Tk()
window.title("PDF to A5 Printable Book") # Nombre de la ventana

window.filename = None

# Creo documento .doc para convertirlo en el pdf_blanco.pdf posteriormente.
# Este pdf_blanco.pdf servirá para rellenar las ubicaciones de páginas cuando sea preciso favoreciendo la paginación.
document = Document()
document.save('test.docx')


##################### Funciones de la aplicación ######################################
# Funciones necesarias para el correcto funcionamiento de la aplicación:

# Función para seleccionar el pdf que se quiere procesar.
def clicked():
    window.filename = filedialog.askopenfilename(initialdir="/home/fraluegut/Descargas", title="Select file", filetypes=(("all files", "*.*"), ("jpeg files", "*.jpg")))

    with open(window.filename, 'rb') as f:
        pdf = PdfFileReader(f)
        numero_pg = pdf.getNumPages()
    numero_paginas_result.configure(text='Número de páginas: ' + str(numero_pg))
    numero_folios_result.configure(text='Número de folios: ' + str(math.ceil(numero_pg/4)))


    return window.filename, numero_pg

# Función para seleccionar el pdf que se quiere procesar.
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

    if math.ceil(numero_pg/20) > 1:
        l.config(text='Se crearán  ' + str(math.ceil(numero_pg / 20)) + " libritos.")
    else:
        l.config(text='Se creará un librito.')
    establecer_n_libritos()
    return numero_folios_reales, input_path

# Función para determinar la ubicación de salida del pdf final y de los intermedios.
def output():
    global path
    path = filedialog.askdirectory()
    output_entry.delete(1, tk.END)  # Remove current text in entry
    output_entry.insert(0, str(path))  # Insert the 'path'
    return path

# Función para dividir en pdf independientes todas las páginas del pdf introducido.
def split(path, name_of_split):
    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        output = f'{name_of_split}{page}.pdf'
        with open(output, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

# Función para determinar la elección de tipo de impresión (1 Cara/Doble Cara).
def print_selection():
     impresora_escogida.config(text='Ha seleccionado ' + var.get())

# Función para determinar el número de libritos que se necesitan teniendo en cuenta el nº de páginas del pdf.
def establecer_n_libritos():
    global conjunto_libros
    # input_path = tk.filedialog.askopenfilename()
    with open(input_path, 'rb') as f:
        pdf = PdfFileReader(f)
        numero_pg = pdf.getNumPages()
    numero_libritos = math.ceil(numero_pg/20)
    print("Dado el número de páginas: " + str(numero_pg) + ", el número de libritos seria " + str(numero_libritos))
    pagina = 0
    conjunto_libros = {}
    for i in range(1, numero_libritos+1):
        libro = "librito_%s" %(i)
        dict={libro:(pagina+1,pagina+20)}
        conjunto_libros.update(dict)


        pagina= pagina + 20
    print("El conjunto de libros sería: ")
    print(conjunto_libros)
    return conjunto_libros

# Esta función es la encargada de realizar el proceso fundamental. Se divide en los siguientes pasos:
# 1.
def procesar():
    global libro_final, librito
    print(input_path)

    split(str(input_path), str(nombre_salida_entry.get())+"_")
    for librito, paginas in conjunto_libros.items():

        print("Librito: " + str(librito) + ". Desde página: " + str(paginas[0]) + ", hasta página " + str(paginas[1]))
        # Matrix con num min de carillas que es el mínimo común múltiplo del número de páginas
        numero_pg = paginas[1]+1-paginas[0]
        numero_folios_reales = math.ceil(numero_pg / 4)
        matrix = np.arange(numero_folios_reales * 4).reshape((numero_folios_reales, 4))
        print("Matrix antigua")
        print(matrix)

        total_paginas=(paginas[0]-1, paginas[1])
        matrix[numero_folios_reales - 1, 2] = statistics.mean(total_paginas) #(numero_folios_reales * 4) / 2
        matrix[numero_folios_reales - 1, 1] = matrix[numero_folios_reales - 1, 2] - 1
        matrix[numero_folios_reales - 1, 3] = matrix[numero_folios_reales - 1, 2] + 1
        matrix[numero_folios_reales - 1, 0] = matrix[numero_folios_reales - 1, 3] + 1

        # TODO Aquí está la miga.
        # for i in range(int(numero_folios_reales) - 2, -1, -1):
        #     print(i)
        #     matrix[i, 0] = matrix[i + 1, 0] + 2
        #     matrix[i, 1] = matrix[i + 1, 1] - 2
        #     matrix[i, 2] = matrix[i + 1, 2] - 2
        #     matrix[i, 3] = matrix[i + 1, 3] + 2

        for i in range(int(numero_folios_reales) - 2, -1, -1):
            print("ID: ")
            print(i)
            matrix[i, 0] = matrix[i + 1, 0] + 2
            matrix[i, 1] = matrix[i + 1, 1] - 2
            matrix[i, 2] = matrix[i + 1, 2] - 2
            matrix[i, 3] = matrix[i + 1, 3] + 2
        print("Matrix: ")
        print(matrix)
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


        Cara_A = PdfFileMerger()

        Cara_B = PdfFileMerger()
        for pdf in Pdfs_cara_A:
            try:
                Cara_A.append(pdf)
            except FileNotFoundError:
                Cara_A.append("pdf_blanco.pdf")
        Cara_A.write(nombre_salida_entry.get() + "_A_"+str(librito))
        for pdf in Pdfs_cara_B:
            try:
                Cara_B.append(pdf)
            except FileNotFoundError:
                Cara_B.append("pdf_blanco.pdf")
        Cara_B.write(nombre_salida_entry.get()+"_B_"+ str(librito))
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

        print("Libritos separados impresos")
    libro_final = PdfFileMerger()
    for librito in conjunto_libros.items():
        libro_final.append(nombre_salida_entry.get() + "_A_" + str(librito[0]))
    for librito in conjunto_libros.items():
        libro_final.append(nombre_salida_entry.get() + "_B_" + str(librito[0]))


    libro_final.write(nombre_salida_entry.get() + "_Final")
    libro_final.close()
    for librito in conjunto_libros.items():
        remove("%s/%s" % (path, nombre_salida_entry.get() + "_A_" + str(librito[0])))
        remove("%s/%s" % (path, nombre_salida_entry.get() + "_B_" + str(librito[0])))
        print("Libros eliminados")

    url_salida = str(output_entry.get()) + "/" + nombre_salida_entry.get() + "_Final"
    # Abre el documento resultante
    wb.open_new(url_salida)

    #os.system(f'start {os.path.realpath(url_salida)}')
    directorio = path.replace("/", "//")
    print(directorio)
    print("Todo salió bien")
    #webbrowser.open(directorio)



##################### Display de la aplicación ######################################
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
impresora_escogida = tk.Label(frame_base, bg='white', width=200, text='')
impresora_escogida.pack(pady=5)



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

# Hueco para texto
l = tk.Label(frame_base, bg='white', width=200, text='')
l.pack(pady=5)

if window.filename is not None:
    a = window.filename


# Dimensiones de la ventana
window.geometry('700x500')
window.mainloop()
