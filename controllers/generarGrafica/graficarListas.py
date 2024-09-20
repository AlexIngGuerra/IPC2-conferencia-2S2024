from utils.estructuras.listaSimple import ListaSimple
from utils.estructuras.listaDoble import ListaDoble
from models.estudiante import Estudiante
from utils.graficar.graficar import generar

def generarListaSimple():
    lista = ListaSimple()
    lista.insertar(Estudiante("persona1", "1"))
    lista.insertar(Estudiante("persona2", "2"))
    lista.insertar(Estudiante("persona3", "3"))
    lista.insertar(Estudiante("persona4", "4"))
    lista.insertar(Estudiante("persona5", "5"))
    lista.insertar(Estudiante("persona6", "6"))
    lista.insertar(Estudiante("persona7", "7"))
    return lista


def generarGraficaListaSimple():
    print("##### Generando Grafica #######")
    lista = generarListaSimple()
    generar(lista.getDot(), "./graficas/listasimple.svg")
    print("##### Grafica Generada #######")
    print("Presione Enter para continuar...")
    input()


def generarListaDoble():
    lista = ListaDoble()
    lista.insertar(Estudiante("estudiante1", "101"))
    lista.insertar(Estudiante("estudiante2", "102"))
    lista.insertar(Estudiante("estudiante3", "103"))
    lista.insertar(Estudiante("estudiante4", "104"))
    lista.insertar(Estudiante("estudiante5", "105"))
    lista.insertar(Estudiante("estudiante6", "106"))
    lista.insertar(Estudiante("estudiante7", "107"))
    return lista


def generarGraficaListaDoble():
    print("##### Generando Grafica #######")
    lista = generarListaDoble()
    generar(lista.getDot(), "./graficas/listadoble.svg")
    print("##### Grafica Generada #######")
    print("Presione Enter para continuar...")
    input()