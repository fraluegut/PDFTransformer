"""import PyPDF2

pdf_file = open('/home/fraluegut/PycharmProjects/PDF_Transformer/sample.pdf')
read_pdf = PyPDF2.PdfFileReader(pdf_file)

number_of_pages = read_pdf.getNumPages()
print(number_of_pages)"""

from PyPDF2 import PdfFileReader, PdfFileWriter
import numpy as np

def extract_information(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

    txt = f"""
    Information about {pdf_path}: 

    Author: {information.author}
    Creator: {information.creator}
    Producer: {information.producer}
    Subject: {information.subject}
    Title: {information.title}
    Number of pages: {number_of_pages}
    """

    print(txt)
    return information


numero_pg = PdfFileReader(open('sample.pdf', 'rb')).getNumPages()

print("Número de páginas del pdf: ")
print(numero_pg)
###################################################################
numero_pg = 9

def numero_carillas(numero_pg):
    if numero_pg % 2 == 0:
        numero_carillas = int(numero_pg /2)
        print("Es par")
    else:
        numero_carillas = int(numero_pg /2) +1
        print("No es par")
    return numero_carillas

def numero_folios(numero_carillas):
    if numero_carillas % 2 == 0:
        numero_folios = int(numero_carillas / 2)
    else:
        numero_folios = int(numero_carillas / 2) + 1
    return numero_folios

print("Número de carillas: ")
print(numero_carillas(numero_pg))

print("Número de folios: ")
print(numero_folios(numero_carillas(numero_pg)))


matriz = np.arange(1,((numero_folios(numero_carillas(numero_pg))* 4)+1)).reshape((numero_folios(numero_carillas(numero_pg)), 4))
print(matriz)

# Reemplazamiento de páginas:
def pagina_central(numero_pg):
    if numero_pg % 2 == 0:
        pagina_central = int(numero_pg / 2)
    else:
        pagina_central = int(numero_pg / 2) + 1
    return pagina_central

print("Página central: ")
pagina_centro = pagina_central(numero_pg)
print("Página centro")
print(pagina_centro)
n_positivo = int(numero_pg / 2)
n_negativo = -int(numero_pg / 2)
print("N_negativo")
print(n_negativo)
print("N_positivo")
print(n_positivo)
n = pagina_centro
numero_mayor = numero_folios(numero_carillas(numero_pg)) * 4
print("Número mayor: ")
print(numero_mayor)
print(n)
for posicion in range(numero_mayor):
    print("Posición ")
    print(posicion)

# Posición central
print("Posición central: ")
posicion_central = numero_mayor -2
print(posicion_central)

# Valor central
valor_central = numero_mayor /2
# Modificación del valor de la posición central:
matriz.put(posicion_central, valor_central)

matriz.put(posicion_central+1, valor_central+1)
matriz.put(posicion_central-1, valor_central-1)

horquilla = range(1,numero_mayor)
"""for x in horquilla:
    posicion_central = 0
    valor_central = 0
    posicion_central = posicion_central + x
    valor_central = valor_central + x
    print(posicion_central)
    matriz.put(posicion_central, valor_central)
    posicion_central = posicion_central - x
    valor_central = valor_central - x
    #matriz.put(posicion_central, valor_central)"""



"""
for x in range(1,n+1):
    print("La x vale: ")
    print(x)
    a = 1
    b = numero_mayor
    #print(int(a*x), int(b*x))
    print(int(a+a*x), int(b-a*x))

    #np.place(matriz, matriz == (numero_mayor-x+1), numero_mayor-x)
    np.place(matriz, matriz == numero_mayor-1, n)
    np.place(matriz, matriz == numero_mayor - 1+x, n+x)
    np.place(matriz, matriz == numero_mayor - 1-x, n - x)
"""
#np.place(matriz, matriz==((numero_folios(numero_carillas(numero_pg))* 4)), pagina_centro+1)
print(matriz)





def split(path, name_of_split):
    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        output = f'{name_of_split}{page}.pdf'
        with open(output, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)





if __name__ == '__main__':
    path = 'sample.pdf'
    #extract_information(path)
    split(path, "Splitado")