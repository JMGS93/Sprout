
tu_pedido = []
total = 0
import time

#Bienvenida
print("Bienvenido a Pizzeria Reale Chusma")
time.sleep(1)
print("Hecha un vistazo al menú!: ")
time.sleep(2)

print("--------MENU--------")
precios = {
    "margarita": 7,
    "mora": 7.50,
    "hawaiana": 8.90,
    "turca": 8.90,
    "tonno": 9.50,
    "5 Formaggi": 10.90,
    "barbacoa": 11.50,
    "reina": 12,
    "caprese": 12}
for key, value in precios.items():
    print(f"{key:12}: {value:.2f}€")
print("--------------------")
time.sleep(2)

#Seleccion de pizza
while True:
    
    pizza = input("Elige la que más te guste! (q to quit): ").lower()
    if pizza == "q":
       break
    elif pizza not in precios:
        print(f"Lo sentimos, {pizza} no esta disponible")
    elif precios.get(pizza) is not None:
        tu_pedido.append(pizza)
    
#Mostrar orden y calcular total > mostrar total 
print("\n------TU PEDIDO------")
for pizza in tu_pedido:
    total += precios.get(pizza)
    print(pizza, end=" ")
print(f"\nEl total es {total:.2f}€")
print("---------------------")
print("Esperamos verte pronto!\nGracias!")
