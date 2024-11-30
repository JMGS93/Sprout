#Vamos a crear un programa de recuento de puntuaciones y veredicto "ganador/perdedor" para los dardos convencionales.

import time
import random
print("Bienvenido!")
time.sleep(1)
print("Vamos a simular una partida a los DARDOS entre 3 concursantes")
time.sleep(2)
print(  "------COMENZAMOS EL JUEGO CON UN CONTADOR DE 121 PUNTOS CADA UNO------")
print(  "---------En cada ronda los jugadores deberán lanzar 3 veces-----------")
print ( "-------El GANADOR será el primero en regresar su CONTADOR a 0---------")
time.sleep(5)
Jug1 = input("Escribe el nombre del primer jugador: ")
Jug2 = input("Escribe el nombre del segundo jugador: ")
Jug3 = input("Escribe el nombre del tercer jugador: ")

menor_num = 1
max_num = 35
random_num1 = random.randint(menor_num, max_num)
random_num2 = random.randint(menor_num, max_num)
random_num3 = random.randint(menor_num, max_num)
random_num4 = random.randint(menor_num, max_num)
random_num5 = random.randint(menor_num, max_num)
random_num6 = random.randint(menor_num, max_num)
random_num7 = random.randint(menor_num, max_num)
random_num8 = random.randint(menor_num, max_num)
random_num9 = random.randint(menor_num, max_num)
random_num10 = random.randint(menor_num, max_num)
random_num11 = random.randint(menor_num, max_num)
random_num12 = random.randint(menor_num, max_num)
random_num13 = random.randint(menor_num, max_num)
random_num14 = random.randint(menor_num, max_num)
random_num15 = random.randint(menor_num, max_num)
random_num16 = random.randint(menor_num, max_num)
random_num17 = random.randint(menor_num, max_num)
random_num18 = random.randint(menor_num, max_num)
random_num19 = random.randint(menor_num, max_num)
random_num20 = random.randint(menor_num, max_num)
random_num21 = random.randint(menor_num, max_num)
random_num22 = random.randint(menor_num, max_num)
random_num23 = random.randint(menor_num, max_num)
random_num24 = random.randint(menor_num, max_num)
random_num25 = random.randint(menor_num, max_num)
random_num26 = random.randint(menor_num, max_num)
random_num27 = random.randint(menor_num, max_num)
total_random1 = random_num1 + random_num2 + random_num3
total_random2 = random_num4 + random_num5 + random_num6
total_random3 = random_num7 + random_num8 + random_num9
total_random4 = random_num10 + random_num11 + random_num12
total_random5 = random_num13 + random_num14 + random_num15
total_random6 = random_num16 + random_num17 + random_num18

dic_puntos = [121,121,121]
dic_puntos[0] = dic_puntos[0] - total_random1
dic_puntos[1] = dic_puntos[1] - total_random2
dic_puntos[2] = dic_puntos[2] - total_random3

#RONDA 1
#PRIMER TURNO Jug1
print("Comencemos!")
print("RONDA 1")
time.sleep(2)
print(f"{Jug1} lanza...")
print(f"{Jug1} lanza y obtiene una puntuación de {random_num1}")
time.sleep(2)
print(f"{Jug1} lanza y obtiene una puntuación de {random_num2}")
time.sleep(2)
print(f"{Jug1} lanza y obtiene una puntuación de {random_num3}")
time.sleep(2)
print(f"{Jug1} ha obtenido un total de {total_random1} puntos!")
print(f"El contador actual de {Jug1} es: {dic_puntos[0]}")
print("----------------------------")

time.sleep(3)

#PRIMER TURNO Jug2
print("Siguiente jugador!")
time.sleep(2)
print(f"{Jug2} lanza...")
print(f"{Jug2} lanza y obtiene una puntuación de {random_num4}")
time.sleep(2)
print(f"{Jug2} lanza y obtiene una puntuación de {random_num5}")
time.sleep(2)
print(f"{Jug2} lanza y obtiene una puntuación de {random_num6}")
time.sleep(2)
print(f"{Jug2} ha obtenido un total de {total_random2} puntos!")
print(f"El contador actual de {Jug2} es: {dic_puntos[1]}")
print("----------------------------")

time.sleep(3)

#PRIMER TURNO Jug3
print("Siguiente jugador!")
time.sleep(2)
print(f"{Jug3} lanza...")
print(f"{Jug3} lanza y obtiene una puntuación de {random_num7}")
time.sleep(2)
print(f"{Jug3} lanza y obtiene una puntuación de {random_num8}")
time.sleep(2)
print(f"{Jug3} lanza y obtiene una puntuación de {random_num9}")
time.sleep(2)
print(f"{Jug3} ha obtenido un total de {total_random3} puntos!")
print(f"El contador actual de {Jug3} es: {dic_puntos[2]}")
print("----------------------------")

time.sleep(3)

puntuaciones = {
    Jug1 : dic_puntos[0],
    Jug2 : dic_puntos[1],
    Jug3 : dic_puntos[2]
}
ganadores = [jugador for jugador, puntuacion in puntuaciones.items() if puntuacion <=0]

if ganadores: 
    print("*************************")
    print("VAYA! Felicidades!")
    print("GANADOR/ES:") 
    for ganador in ganadores: 
        print(ganador)
    print("El juego ha finalizado!")
    print("Hasta la próxima!")
    print("*************************")
    exit()
else:
    print("Contadores actuales de los concursantes: ")
    print(dic_puntos)
    time.sleep(3)
    print("----------------------------")
    print("RONDA 2")


#--------------------------------------------------------------------------------


#RONDA 2
#SEGUNDO TURNO Jug1
time.sleep(2)
print(f"{Jug1} lanza...")
print(f"{Jug1} lanza y obtiene una puntuación de {random_num10}")
time.sleep(2)
print(f"{Jug1} lanza y obtiene una puntuación de {random_num11}")
time.sleep(2)
print(f"{Jug1} lanza y obtiene una puntuación de {random_num12}")
time.sleep(2)
print(f"{Jug1} ha obtenido un total de {total_random4} puntos!")
dic_puntos[0] -= total_random4
print(f"El contador actual de {Jug1} es: {dic_puntos[0]}")
print("----------------------------")

time.sleep(3)

#SEGUNDO TURNO Jug2
print("Siguiente jugador!")
time.sleep(2)
print(f"{Jug2} lanza...")
print(f"{Jug2} lanza y obtiene una puntuación de {random_num13}")
time.sleep(2)
print(f"{Jug2} lanza y obtiene una puntuación de {random_num14}")
time.sleep(2)
print(f"{Jug2} lanza y obtiene una puntuación de {random_num15}")
time.sleep(2)
print(f"{Jug2} ha obtenido un total de {total_random5} puntos!")
dic_puntos[1] -= total_random5
print(f"El contador actual de {Jug2} es: {dic_puntos[1]}")
print("----------------------------")

time.sleep(3)

#SEGUNDO TURNO Jug3
print("Siguiente jugador!")
time.sleep(2)
print(f"{Jug3} lanza...")
print(f"{Jug3} lanza y obtiene una puntuación de {random_num16}")
time.sleep(2)
print(f"{Jug3} lanza y obtiene una puntuación de {random_num17}")
time.sleep(2)
print(f"{Jug3} lanza y obtiene una puntuación de {random_num18}")
time.sleep(2)
print(f"{Jug3} ha obtenido un total de {total_random6} puntos!")
dic_puntos[2] -= total_random6
print(f"El contador actual de {Jug3} es: {dic_puntos[2]}")
print("----------------------------")

time.sleep(3)

puntuaciones = {
    Jug1 : dic_puntos[0],
    Jug2 : dic_puntos[1],
    Jug3 : dic_puntos[2]
}
ganadores = [jugador for jugador, puntuacion in puntuaciones.items() if puntuacion <=0]

if ganadores: 
    print("*************************")
    print("VAYA! Felicidades!")
    print("GANADOR/ES:") 
    for ganador in ganadores: 
        print(ganador)
    print("El juego ha finalizado!")
    print("Hasta la próxima!")
    print("*************************")
    exit()
else:
    print("Contadores actuales de los concursantes: ")
    print(dic_puntos)
    time.sleep(3)
print("----------------------------")
print("RONDA 3")

#------------------------------------------------------------------------------- 

#RONDA 3
#TERCER TURNO Jug1
time.sleep(2)
print(f"{Jug1} lanza...")
print(f"{Jug1} lanza y obtiene una puntuación de {random_num19}")
time.sleep(2)
print(f"{Jug1} lanza y obtiene una puntuación de {random_num11}")
time.sleep(2)
print(f"{Jug1} lanza y obtiene una puntuación de {random_num12}")
time.sleep(2)
print(f"{Jug1} ha obtenido un total de {total_random4} puntos!")
dic_puntos[0] -= total_random4
print(f"El contador actual de {Jug1} es: {dic_puntos[0]}")
print("----------------------------")


time.sleep(3)

#TERCER TURNO Jug2
print("Siguiente jugador!")
time.sleep(2)
print(f"{Jug2} lanza...")
print(f"{Jug2} lanza y obtiene una puntuación de {random_num13}")
time.sleep(2)
print(f"{Jug2} lanza y obtiene una puntuación de {random_num14}")
time.sleep(2)
print(f"{Jug2} lanza y obtiene una puntuación de {random_num15}")
time.sleep(2)
print(f"{Jug2} ha obtenido un total de {total_random5} puntos!")
dic_puntos[1] -= total_random5
print(f"El contador actual de {Jug2} es: {dic_puntos[1]}")
print("----------------------------")


time.sleep(3)

#TERCER TURNO Jug3
print("Siguiente jugador!")
time.sleep(2)
print(f"{Jug3} lanza...")
print(f"{Jug3} lanza y obtiene una puntuación de {random_num16}")
time.sleep(2)
print(f"{Jug3} lanza y obtiene una puntuación de {random_num17}")
time.sleep(2)
print(f"{Jug3} lanza y obtiene una puntuación de {random_num18}")
time.sleep(2)
print(f"{Jug3} ha obtenido un total de {total_random6} puntos!")
dic_puntos[2] -= total_random6
print(f"El contador actual de {Jug3} es: {dic_puntos[2]}")
print("----------------------------")

time.sleep(3)

puntuaciones = {
    Jug1 : dic_puntos[0],
    Jug2 : dic_puntos[1],
    Jug3 : dic_puntos[2]
}
ganadores = [jugador for jugador, puntuacion in puntuaciones.items() if puntuacion <=0]

if ganadores:
    print("*************************")
    print("VAYA! Felicidades!")
    print("GANADOR/ES:")  
    for ganador in ganadores: 
        print(ganador)
    print("El juego ha finalizado!")
    print("Hasta la próxima!")
    print("*************************")
    exit()
else:
    print("Contadores actuales de los concursantes: ")
    print(dic_puntos)
    time.sleep(3)
    print("VAYA! Se han agotado el numero de intentos!")
    print("El juego finaliza sin ningún ganador!")
    print("Suerte la próxima vez!")
   