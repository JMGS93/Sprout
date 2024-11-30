#Vamos a crear un conversor de unidades de peso
peso = float(input("Porfavor, introduce tu peso: "))
unidad = input("Kilogramos o Libras? (K or L): ")
if unidad == "K":
    peso = round(peso * 2.205, 2)
    print(f"Tu peso es de {peso}lbs")
else:
    peso = round(peso / 2.205)
    print(f"Tu peso es de {peso}kgs")