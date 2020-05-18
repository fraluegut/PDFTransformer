"""import PyPDF2

pdf_file = open('/home/fraluegut/PycharmProjects/PDF_Transformer/sample.pdf')
read_pdf = PyPDF2.PdfFileReader(pdf_file)

number_of_pages = read_pdf.getNumPages()
print(number_of_pages)"""

from PyPDF2 import PdfFileReader, PdfFileWriter
import numpy as np
import glob

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


#numero_pg = PdfFileReader(open('Desobediencia_civil.pdf', 'rb')).getNumPages()
numero_pg = 12
print("Número de páginas del pdf: ")
print(numero_pg)

# Nº folios:
print("Número de folios: ")
print(numero_pg/4)
###################################################################
num2 = 4
def mcd(num1, num2):
    a = max(num1, num2)
    b = min(num1, num2)
    while b!=0:
        mcd = b
        b = a%b
        a = mcd
    return mcd

def mcm(num1, num2):
    a = max(num1, num2)
    b = min(num1, num2)
    mcm = (a / mcd(a,b)) * b
    return mcm

min_comun_multiplo_del_n_pg = mcm(numero_pg, 4)
print(min_comun_multiplo_del_n_pg)
###################################################################
# Matrix con num min de carillas que es el mínimo común múltiplo del número de páginas
matrix = np.arange(int(min_comun_multiplo_del_n_pg)).reshape((int(min_comun_multiplo_del_n_pg/4),4))
print(matrix)

matrix[0,0] = int(numero_pg)
matrix[0,1] = 1
matrix[0,2] = 2
matrix[0,3] = numero_pg - 1
print("Nueva tabla")

for i in range(1, int(numero_pg/4)):
    matrix[i, 0] = matrix[i-1, 0] - 2
    matrix[i, 1] = matrix[i-1, 1] + 2
    matrix[i, 2] = matrix[i-1, 2] + 2
    matrix[i, 3] = matrix[i-1, 3] - 2

print(matrix[2-1, 0])
print(matrix)
"""
numero_pg = 16

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
"""
# Reemplazamiento de páginas:
"""def pagina_central(numero_pg):
    if numero_pg % 2 == 0:
        pagina_central = int(numero_pg / 2)
    else:
        pagina_central = int(numero_pg / 2) + 1
    return pagina_central
"""
"""print("Página central: ")
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


# Posición central
print("Posición central: ")
posicion_central = numero_mayor -2
print(posicion_central)

# Valor central
valor_central = numero_mayor /2
# Modificación del valor de la posición central:
"""
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
"""
print("Nuevo Esquema: ")
print(matriz)

numero_mayor = 16
numero_menor = 1

lista = (1,3,1,3,1,3)
def ascension(numero_mayor, numero_menor):
    posicion_inicio = 2
    posicion_final = 1
    np.place(matriz, matriz == posicion_final, numero_mayor)
    np.place(matriz, matriz == posicion_inicio, numero_menor)
    for x in lista:
        for i in range(numero_mayor):
            np.place(matriz, matriz == posicion_inicio+i, numero_menor+1)
            print(i)
            posicion_inicio = posicion_inicio + x
        return posicion_inicio

#posicion_inicio+lista[x]
ascension(numero_mayor, numero_menor)
print(matriz)

print("CODIFICACIÓN")
codificacion = []

for i in range(int(int(numero_mayor)/2)):
    codificacion.append(1)
    codificacion.append(3)

print(codificacion)


for x in range(numero_mayor):
    matriz

# DIVIDIR PDF
def split(path, name_of_split):
    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        output = f'{name_of_split}{page}.pdf'
        with open(output, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

# UNIR PDF
def merger(output_path, input_paths):
    pdf_writer = PdfFileWriter()
    for path in input_paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))
    with open(output_path, 'wb') as fh:
        pdf_writer.write(fh)
"""












if __name__ == '__main__':
    path = 'Desobediencia_civil.pdf'
    #extract_information(path)

    #split(path, "Desobediencia_civil_")

    #paths = glob.glob('w9_*.pdf')
    #paths.sort()
    #merger('pdf_merger.pdf', paths)