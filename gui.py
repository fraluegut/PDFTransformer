from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from main import extract_information

window = Tk()

window.title("PDF to A5 Printable Book")

lbl = Label(window, text="")
lbl.grid(column=0, row=2)


#txt = Entry(window,width=10)
#txt.grid(column=1, row=0)

window.filename = None
def clicked():
    window.filename = filedialog.askopenfilename(initialdir="/home/fraluegut/Descargas", title="Select file", filetypes=(("all files", "*.*"), ("jpeg files", "*.jpg")))
    data = extract_information(window.filename).number_of_pages
    lbl.configure(text="Hola")
    print(window.filename)
    print(data)
    return window.filename
btn = Button(window, text="Seleccionar documento", command=clicked)
btn.grid(column=1, row=0)

if window.filename is not None:
    a = window.filename
    print(a)


window.geometry('350x200')
window.mainloop()