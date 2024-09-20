
class Estudiante:

    def __init__(self, nombre, carnet):
        self.nombre = nombre 
        self.carnet = carnet

    def toDotString(self):
        return f'{self.nombre}\\n{self.carnet}'
