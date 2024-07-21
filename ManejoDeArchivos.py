#Ejercicio 9
with open("archivo.txt", "w") as archivo:
    archivo.write("Hola, este es un archivo de texto.")

with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)