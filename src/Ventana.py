import tkinter as tk
from tkinter import messagebox

def mostrear_mensaje():
    messagebox.showinfo("AVISO", "¡BOTÓN PRESIONADO!")
ventana = tk.Tk()
ventana.title("Ventana simple")

label = tk.Label(ventana, text="Presiona el botón para ver un mensaje")
label.pack(pady=10)

boton = tk.Button(ventana, text="Haz clic aquí", command=mostrear_mensaje)
boton.pack()

ventana.mainloop()