from os import system
from controllers.generarGrafica.graficarListas import generarGraficaListaSimple
from controllers.generarGrafica.graficarListas import generarGraficaListaDoble


def menu():
    while True:
        system("cls")
        print("########### MENU PRINCIPAL ############")
        print("1. Graficar Lista Simple")
        print("2. Graficar Lista Doble")
        print("3. Salir")

        opcion = input()
        if opcion == "1":
            generarGraficaListaSimple()
        elif opcion == "2":
            generarGraficaListaDoble()
        elif opcion == "3":
            break