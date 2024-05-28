import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import Toplevel
from Estructuras.arbol_avl import ArbolAVL
from Objetos.Objeto import Objeto

class VentanaPrincipal(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("ARBOL AVL")
        self.geometry("800x600")

        self.arbol_avl = ArbolAVL()

        frame = ttk.Frame(self)
        frame.pack(expand=True, fill='both')

        # Left frame for inputs
        input_frame = ttk.Frame(frame)
        input_frame.grid(row=0, column=0, padx=10, pady=10, sticky='nw')

        # Labels and Entries
        label_valor = ttk.Label(input_frame, text="ID")
        label_valor.grid(row=0, column=0, pady=5, sticky='w')
        self.entry_valor = ttk.Entry(input_frame)
        self.entry_valor.grid(row=0, column=1, pady=5)

        label_nombre = ttk.Label(input_frame, text="Nombre")
        label_nombre.grid(row=1, column=0, pady=5, sticky='w')
        self.entry_nombre = ttk.Entry(input_frame)
        self.entry_nombre.grid(row=1, column=1, pady=5)

        label_color = ttk.Label(input_frame, text="Numero telefonico")
        label_color.grid(row=2, column=0, pady=5, sticky='w')
        self.entry_color = ttk.Entry(input_frame)
        self.entry_color.grid(row=2, column=1, pady=5)

        label_edad = ttk.Label(input_frame, text="Edad")
        label_edad.grid(row=3, column=0, pady=5, sticky='w')
        self.entry_edad = ttk.Entry(input_frame)
        self.entry_edad.grid(row=3, column=1, pady=5)

        self.boton_insertar = ttk.Button(input_frame, text="Insertar", command=self.insertar_valor)
        self.boton_insertar.grid(row=4, column=0, columnspan=2, pady=10)

        label_valor2 = ttk.Label(input_frame, text="ID eliminar")
        label_valor2.grid(row=5, column=0, pady=5, sticky='w')
        self.entry_valor2 = ttk.Entry(input_frame)
        self.entry_valor2.grid(row=5, column=1, pady=5)

        self.boton_eliminar = ttk.Button(input_frame, text="Eliminar", command=self.eliminar_valor)
        self.boton_eliminar.grid(row=6, column=0, columnspan=2, pady=10)

        label_valor3 = ttk.Label(input_frame, text="ID buscar")
        label_valor3.grid(row=7, column=0, pady=5, sticky='w')
        self.entry_valor3 = ttk.Entry(input_frame)
        self.entry_valor3.grid(row=7, column=1, pady=5)

        self.boton_buscar = ttk.Button(input_frame, text="Buscar", command=self.buscar_valor)
        self.boton_buscar.grid(row=8, column=0, columnspan=2, pady=10)

        self.boton_listar = ttk.Button(input_frame, text="Listar", command=self.listar)
        self.boton_listar.grid(row=9, column=0, columnspan=2, pady=10)

        self.canvas = tk.Canvas(frame, bg='white', width=600, height=400)
        self.canvas.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

        frame.grid_columnconfigure(1, weight=1)
        frame.grid_rowconfigure(0, weight=1)

    def listar(self):
        messagebox.showinfo("ID", "Se muestra en terminal")

    def eliminar_valor(self):
        id = int(self.entry_valor2.get())
        self.arbol_avl.elimina(id)
        self.dibujar_arbol()

    def buscar_valor(self):
        id = int(self.entry_valor3.get())
        text = self.arbol_avl.buscar(id)
        messagebox.showinfo("ID", (f"ID: {text.objeto.id}\nNombre: {text.objeto.nombre}\nNumero telefonico: {text.objeto.color}\nEdad: {text.objeto.edad}"))
        self.dibujar_arbol()

    def insertar_valor(self):
        valor = int(self.entry_valor.get())
        nombre = self.entry_nombre.get()
        color = self.entry_color.get()
        edad = self.entry_edad.get()
        objeto = Objeto(valor, nombre, color, edad)
        self.arbol_avl.insert(objeto)
        self.dibujar_arbol()

    def dibujar_arbol(self):
        self.canvas.delete("all")
        if self.arbol_avl.raiz is not None:
            self.arbol_avl.dibujar_arbol(self.canvas, self.arbol_avl.raiz, 400, 50, 100, 0)
            
def main():
    root = tk.Tk()  
    root.withdraw()  
    ventana_principal = VentanaPrincipal(root)
    ventana_principal.mainloop()