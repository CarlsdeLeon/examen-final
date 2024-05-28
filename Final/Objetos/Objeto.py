class Objeto:
    def __init__(self, id, nombre, color, edad):
        self.id = id
        self.nombre = nombre
        self.color = color
        self.edad = edad
        
    def __str__(self):
        return f"ID: {self.id}"
        