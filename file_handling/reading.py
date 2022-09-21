# Hay tres modos para leer un archivo con la funcion open()

# "r" para leer
# "a" para agregar al final (append)
# "w" para sobre escribir el contenido

file = open('file_handling/sample.txt,"r"', encondings="UTF-8")
# la funcion open entrega un "objeto". Entenderemos un objeto
# como algo que tiene "datos" y "metodos". los metodos son para manipular sus datos

print(file)

# para leer el contenido del objeto file, tenemos el metodo del objeto
# read()

print(file.read())
