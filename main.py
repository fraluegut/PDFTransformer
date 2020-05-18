"""import PyPDF2

pdf_file = open('/home/fraluegut/PycharmProjects/PDF_Transformer/sample.pdf')
read_pdf = PyPDF2.PdfFileReader(pdf_file)

number_of_pages = read_pdf.getNumPages()
print(number_of_pages)"""

from PyPDF2 import PdfFileReader, PdfFileMerger, PdfFileWriter
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


numero_pg = PdfFileReader(open('Desobediencia_civil.pdf', 'rb')).getNumPages()
#numero_pg = 40
print("Número de páginas del pdf: ")
print(numero_pg)

# Nº folios:
print("Número de folios teórico: ")
print(numero_pg/4)
###################################################################

# Redondeo forzado hacia arriba
import math
#math.ceil(1.1)

# Número de folios reales:
numero_folios_reales = math.ceil(numero_pg/4)
print("Número de folios reales:")
print(numero_folios_reales)

###################################################################
# Matrix con num min de carillas que es el mínimo común múltiplo del número de páginas
matrix = np.arange(numero_folios_reales*4).reshape((numero_folios_reales,4))

# Matriz base:
print("Matriz base:")
print(matrix)


matrix[numero_folios_reales-1,2] = (numero_folios_reales*4)/2
matrix[numero_folios_reales-1,1] = matrix[numero_folios_reales-1,2] -1
matrix[numero_folios_reales-1,3] = matrix[numero_folios_reales-1,2] +1
matrix[numero_folios_reales-1,0] = matrix[numero_folios_reales-1,3] +1


for i in range(int(numero_folios_reales)-2, -1, -1):
    #print(i)
    matrix[i, 0] = matrix[i+1, 0] + 2
    matrix[i, 1] = matrix[i+1, 1] - 2
    matrix[i, 2] = matrix[i+1, 2] - 2
    matrix[i, 3] = matrix[i+1, 3] + 2

print("Matriz definitiva")
print(matrix)

#######################################################################
#Merge pdf

pdf_page = "jose"
print("Desobediencia_civil_%s.pdf" % pdf_page)
lista_pdfs_cara_A = []

for i in range(0, numero_folios_reales):
        lista_pdfs_cara_A.append("Desobediencia_civil_%s.pdf" % matrix[i,0])
        lista_pdfs_cara_A.append("Desobediencia_civil_%s.pdf" % matrix[i, 1])

print(lista_pdfs_cara_A)
#pdfs = ["Desobediencia_civil_%s.pdf" % name]

merger = PdfFileMerger()

for pdf in lista_pdfs_cara_A:
    merger.append(pdf)

merger.write("Cara_A.pdf")
merger.close()

if __name__ == '__main__':
    path = 'Desobediencia_civil.pdf'
    extract_information(path)

    #split(path, "Desobediencia_civil_")

    paths = glob.glob('w9_*.pdf')
    paths.sort()
    merger('pdf_merger.pdf', paths)