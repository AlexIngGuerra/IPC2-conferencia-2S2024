class Nodo:

    def __init__(self, data):
        self.data = data
        self.siguiente = None

class ListaSimple:

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

    # Generar grafica en dot
    def getDot(self):
        if(self.inicio == None):
            print("### Error: Lista vacia")
            return ""
        
        idNodo = 0
        cadena = "digraph G {\nnode[shape=record];\nrankdir=\"LR\";\n"

        idNodo += 1
        dotNode = "{} [label=\"{}\"];\n".format(idNodo, self.inicio.data.toDotString())
        cadena = cadena + dotNode

        aux = self.inicio.siguiente
        while aux != None:
            idNodo += 1
            dotNode = "{} [label=\"{}\"];\n".format(idNodo, aux.data.toDotString())
            dotNext = "{}->{};\n".format(idNodo-1, idNodo)
            cadena = cadena + dotNode + dotNext
            aux = aux.siguiente

        cadena = cadena + "\n}"
        return cadena
        