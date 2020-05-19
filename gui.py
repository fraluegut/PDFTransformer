from tkinter import *
from tkinter import messagebox

window = Tk()

window.title("PDF to A5 Printable Book")

lbl = Label(window, text="Título del archivo")

lbl.grid(column=0, row=0)


txt = Entry(window,width=10)

txt.grid(column=1, row=0)
def clicked():

    messagebox.showinfo('Notificación', 'Enviado')

btn = Button(window, text="Enviar", command=clicked)

btn.grid(column=4, row=4)
window.geometry('350x200')
window.mainloop()