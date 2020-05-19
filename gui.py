from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

window = Tk()

window.title("PDF to A5 Printable Book")

lbl = Label(window, text="Título del archivo")

lbl.grid(column=0, row=0)


txt = Entry(window,width=10)

txt.grid(column=1, row=0)
window.filename = None
def clicked():
    window.filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    print(window.filename)
    return window.filename
btn = Button(window, text="Enviar", command=clicked)
btn.grid(column=4, row=4)

if window.filename is not None:
    a = window.filename
    print(a)


window.geometry('350x200')
window.mainloop()