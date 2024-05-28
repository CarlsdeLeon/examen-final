import tkinter as tk

class Nodo:
    def __init__(self, objeto):
        self.objeto = objeto
        self.izquierda = None
        self.derecha = None
        self.altura = 1

    @property
    def id(self):
        return self.objeto.id

class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def rotacion_derecha(self, z):
        y = z.izquierda
        x = y.derecha

        y.derecha = z
        z.izquierda = x

        z.altura = 1 + max(self.obtener_altura(z.izquierda), self.obtener_altura(z.derecha))
        y.altura = 1 + max(self.obtener_altura(y.izquierda), self.obtener_altura(y.derecha))

        return y

    def rotacion_izquierda(self, z):
        y = z.derecha
        x = y.izquierda

        y.izquierda = z
        z.derecha = x

        z.altura = 1 + max(self.obtener_altura(z.izquierda), self.obtener_altura(z.derecha))
        y.altura = 1 + max(self.obtener_altura(y.izquierda), self.obtener_altura(y.derecha))

        return y

    def rotacion_derecha_izquierda(self, z):
        z.derecha = self.rotacion_derecha(z.derecha)
        return self.rotacion_izquierda(z)

    def rotacion_izquierda_derecha(self, z):
        z.izquierda = self.rotacion_izquierda(z.izquierda)
        return self.rotacion_derecha(z)

    def obtener_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def obtener_balance(self, nodo):
        if not nodo:
            return 0
        return self.obtener_altura(nodo.izquierda) - self.obtener_altura(nodo.derecha)

    def insert(self, objeto):
        self.raiz = self.insertar(self.raiz, objeto)

    def insertar(self, raiz, objeto):
        if not raiz:
            return Nodo(objeto)
        elif objeto.id < raiz.id:
            raiz.izquierda = self.insertar(raiz.izquierda, objeto)
        else:
            raiz.derecha = self.insertar(raiz.derecha, objeto)
        return raiz

    def elimina(self, id):
        self.raiz = self.eliminar(self.raiz, id)
    def eliminar(self, raiz, valor):
        if raiz is None:
            return raiz

        if valor < raiz.objeto.id:
            raiz.izquierda = self.eliminar(raiz.izquierda, valor)
        elif valor > raiz.objeto.id:
            raiz.derecha = self.eliminar(raiz.derecha, valor)
        else:
            if raiz.izquierda is None:
                temp = raiz.derecha
                raiz = None
                return temp
            elif raiz.derecha is None:
                temp = raiz.izquierda
                raiz = None
                return temp

            temp = self.sucesor_inmediato(raiz.derecha)
            raiz.objeto.id = temp.objeto.id
            raiz.derecha = self.eliminar(raiz.derecha, temp.objeto.id)
        return raiz

    def sucesor_inmediato(self, nodo):
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual

    def buscar(self, id):
        return self.busqueda_binaria(self.raiz, id)

    def busqueda_binaria(self, raiz, codigo):
        if raiz is None or raiz.objeto.id == codigo:
            return raiz
        if codigo < raiz.objeto.id:
            return self.busqueda_binaria(raiz.izquierda, codigo)
        return self.busqueda_binaria(raiz.derecha, codigo)

    def inorden(self):
        self.mostrar_inorden(self.raiz)
    def mostrar_inorden(self, raiz):
        if raiz is not None:
            self.mostrar_inorden(raiz.izquierda)
            print(raiz.valor, end=' ')
            self.mostrar_inorden(raiz.derecha)

    def dibujar_arbol(self, canvas, nodo, x, y, dx, nivel):
        if nodo is not None:
            canvas.create_text(x, y, text=str(nodo.objeto), font=("Helvetica", 12), tags="text")
            if nodo.izquierda:
                canvas.create_line(x, y, x - dx, y + 50, arrow=tk.LAST, tags="line")
                self.dibujar_arbol(canvas, nodo.izquierda, x - dx, y + 50, dx // 2, nivel + 1)
            if nodo.derecha:
                canvas.create_line(x, y, x + dx, y + 50, arrow=tk.LAST, tags="line")
                self.dibujar_arbol(canvas, nodo.derecha, x + dx, y + 50, dx // 2, nivel + 1)




