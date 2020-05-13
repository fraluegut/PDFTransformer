"""import PyPDF2

pdf_file = open('/home/fraluegut/PycharmProjects/PDF_Transformer/sample.pdf')
read_pdf = PyPDF2.PdfFileReader(pdf_file)

number_of_pages = read_pdf.getNumPages()
print(number_of_pages)"""

from PyPDF2 import PdfFileReader, PdfFileWriter


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

numero_pg = 9
def numero_carillas(numero_pg):
    if numero_pg % 2 == 0:
        numero_carillas = numero_pg /2
        print("Es par")
    else:
        numero_carillas = int(numero_pg /2) +1
        print("No es par")
    return numero_carillas

def numero_folios(numero_carillas):
    if numero_carillas % 2 == 0:
        numero_folios = numero_carillas / 2
    else:
        numero_folios = int(numero_carillas / 2) + 1


print("Número de carillas: ")
print(numero_carillas(numero_pg))

def split(path, name_of_split):
    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        output = f'{name_of_split}{page}.pdf'
        with open(output, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)



print("Prueba: ")
print(33 % 2)



if __name__ == '__main__':
    path = 'sample.pdf'
    #extract_information(path)
    split(path, "Splitado")