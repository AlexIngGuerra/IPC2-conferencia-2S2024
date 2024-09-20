from os import system

def menu():
    while True:
        system("cls")
        print("########### MENU PRINCIPAL ############")
        print("1. Graficar Lista Simple")
        print("2. Graficar Lista Doble")
        print("3. Salir")

        opcion = input()
        if opcion == "1":
            print("Graficando lista simple")
        elif opcion == "2":
            print("Graficando lista doble")
        elif opcion == "3":
            break