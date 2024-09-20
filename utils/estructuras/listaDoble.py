class Nodo:

    def __init__(self, data):
        self.data = data
        self.siguiente = None
        self.anterior = None

class ListaDoble:

    def __init__(self):
        self.inicio = None

    # Funcion para insertar nuevo dato
    def insertar(self, data):
        nuevo = Nodo(data)

        if self.inicio == None:
            self.inicio = nuevo
            return
        
        aux = self.inicio
        while aux.siguiente != None:
            aux = aux.siguiente
        
        aux.siguiente = nuevo
        nuevo.anterior = aux