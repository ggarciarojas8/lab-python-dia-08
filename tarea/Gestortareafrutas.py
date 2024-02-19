# Función para agregar una nueva fruta a la lista de frutas
def agregar_fruta(fruta, lista_frutas):
    lista_frutas.append(fruta)
    print("Fruta agregada exitosamente.")

# Función para mostrar todas las frutas en la lista
def mostrar_frutas(lista_frutas):
    if lista_frutas:
        print("Lista de frutas:")
        for i, fruta in enumerate(lista_frutas, start=1):
            print(f"{i}. {fruta}")
    else:
        print("No hay frutas pendientes por comprar.")

# Función para marcar una fruta como comprada
def comprar_fruta(numero_fruta, lista_frutas):
    if 1 <= numero_fruta <= len(lista_frutas):
        fruta_comprada = lista_frutas.pop(numero_fruta - 1)
        print(f"Fruta '{fruta_comprada}' comprada.")
    else:
        print("Número de fruta inválido.")

# Función para guardar las frutas en un archivo de texto
def guardar_frutas(nombre_archivo, lista_frutas):
    try:
        with open(nombre_archivo, 'w') as archivo:
            for fruta in lista_frutas:
                archivo.write(fruta + '\n')
        print("Frutas guardadas en el archivo correctamente.")
    except IOError:
        print("Error al guardar las tareas en el archivo.")
# Lista para almacenar las frutas
frutas = []

# Menú principal
while True:
    print("\n--- GESTIÓN DE FRUTAS ---")
    print("1. Agregar fruta")
    print("2. Mostrar frutas")
    print("3. Comprar frutas")
    print("4. Guardar frutas")
    print("5. Salir")

    opcion = input("Ingrese el número de la opción que desea: ")

    if opcion == '1':
        nueva_fruta = input("Ingrese la nueva fruta: ")
        agregar_fruta(nueva_fruta, frutas)
    elif opcion == '2':
        mostrar_frutas(frutas)
    elif opcion == '3':
        if frutas:
            mostrar_frutas(frutas)
            num_fruta_comprada = int(input("Ingrese el número de la fruta comprada: "))
            comprar_fruta(num_fruta_comprada, frutas)
        else:
            print("No hay Frutas para comprar.")
    elif opcion == '4':
        nombre_archivo = input("Ingrese el nombre del archivo para guardar las frutas: ")
        guardar_frutas(nombre_archivo, frutas)
    elif opcion == '5':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 5.")