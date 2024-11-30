#Vamos a crear un conversor de medidas de temperatura
temp = float(input("Porfavor, introduce la temperatura: "))
unidad = input("Celsius o Fahrenheit? (C or F): ").upper()

while unidad =="":
    print("No has introducido nada")
    unidad = input("Celsius o Fahrenheit? (C or F): ").upper()
if unidad == "C":
    temp = round((temp * 9) / 5 + 32, 2)
    print(f"La temperatura es de {temp}º Fahrenheit")
    print("Hasta pronto!")
elif unidad == "F":
    temp = round((temp - 32) * 5 / 9, 2)
    print(f"La temperatura es de {temp}º Celsius")
    print("Hasta pronto!")
else:
    print(f"Lo siento, {unidad} no es una medida valida.")
