# Tenemos expresiones que se pueden evaluar en terminos booleanos
# o dicotomicos
# Ejemplo:

print(10 > 9)

# Esto nos permite hacer ejecuciones condicionales, por ejemplo

def is_adult(age):
    if age>= 18:
        return True
    else:
        return False        

gaby_age = 30
paola_age = 30

# Estas siguentes intrucciones las podriamos leer como:
# "Si el resultado de is_adult ejecutada con la variable gaby_age o paola_age
# es verdadero, entonces el programa imprime '¿quieres una cerveza'
# De otro modo (else), imrprime 'Cantemos chuchuwa?'"

if is_adult(paola_age):
    print("¿Quieres una cerveza?")
else:
    print("Cantemos Chuchuwa?")

# elif es una abreviacion "else if", nos permite seguir evaluendo expresiones. Podemos tener tantos como necesitemos

if (paola_age > gaby_age):
    print("Paola es mayor que Gaby", paola_age - gaby_age,"años mas")
elif paola_age < gaby_age:
    print("Paola es menor que Gaby")    
else:
    print("Tienen la misma edad Gaby y Paola")    
