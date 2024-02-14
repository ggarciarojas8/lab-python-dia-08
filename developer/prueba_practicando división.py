'''
    En este código, vamos a sumar el valor de las variables
    numero_1
    numero_2
    numero_3
    numero_4
    Sin embargo, el valor de estas variables es ingresado por el usuario.
'''
# La suma de cuatro números
print("Suma de cuatro números")

# Se solicita al usuario que ingrese el valor del primer número y se guarda en la variable numero_1
numero_1 = input("Intro número uno ") # El input nos ayuda a ingresar valores desde el teclado

# Se solicita al usuario que ingrese el valor del segundo número y se guarda en la variable numero_2
numero_2 = input("Intro número dos ")

# Se solicita al usuario que ingrese el valor del tercer número y se guarda en la variable numero_3
numero_3 = input("Intro número tres ")

# Se solicita al usuario que ingrese el valor del cuarto número y se guarda en la variable numero_4
numero_4 = input("Intro número cuatro ")

# Se convierten los valores ingresados por el usuario a enteros (int) y se suman
resultado_suma = int(numero_1) + int(numero_2)+ int(numero_3)+ int(numero_4)

# Se imprime el resultado de la suma utilizando una f-string para formatear el mensaje
print(f"El resultado de la suma es: {resultado_suma}")