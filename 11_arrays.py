# Los arreglos (LISTAS) son una ESTRUCTURA DE DATOS FUNDAMENTAL
#que permite agrupar valores, separados por COMA. 

first_array = ['Sacar la basura', 'peinarse', 'domir','secar la ropa']

# En python el primer elemento de un arreglo tiene posicion (indice) 0
print(first_array[0])

print(first_array[1])
print(first_array[2])
print(first_array[3])
# No existe el elemento con indice 4 y python da un error
# print(first_array[4])

# Podemos saber el largo de un arreglo o lista con la funcion pre definida len()

print(len(first_array))

# Ademas, podemos agregar elementos al arreglo
first_array.append('Comer')
first_array.append('Dormir')

# Podemos indicar la posicion del nuevo elemento a  agragar con insert
first_array.insert(0,'Levantarse')

# Podemos imprimir la lista completa
print(first_array)

