import subprocess

def generar(contenido, salida):
    try:
        # Ruta para el ejecutable dot
        ruta_dot = "dot"

        # Ruta del archivo a generar
        archivodot = "./utils/graficar/grafo.dot"

        # Crear y escribir el archivo dot
        with open(archivodot, "w") as file:
            file.write(contenido)

        # Generar grafica
        # dot -Tsvg grafo.dot -o grafo.svg
        comando = [ruta_dot, "-Tsvg", archivodot, "-o", salida]
        subprocess.run(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
    except Exception as e:
        print(e)