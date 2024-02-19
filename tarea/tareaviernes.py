#Lista de Personas
personas = ["Monica", "Camila", "Valeska", "María José", "Fernando", "Guillermo"]

#Le pregunta al usuario a la persona que quiere conocer
consulta = input(f"A qué persona quieres conocer {personas}:")


if consulta.lower() == "monica":
    print("Monica es esposa de Guillermo")
elif consulta.lower() == "camila":
    print("Camila es Hija Mayor de Mónica y Guillermo")
elif consulta.lower() == "valeska":
    print("Valeska es hija segunda de Mónica y Guillermo")
elif consulta.lower() == "maría jose":
    print("María José es hija tercera de Mónica y Guillermo")
elif consulta.lower() == "fernando":
    print("Fernando es hijo cuarto de Mónica y Guillermo")
elif consulta.lower() == "guillermo":
    print("Guillermo es esposo de Mónica")
else:
    print(f"{consulta} no esta en la lista")    
