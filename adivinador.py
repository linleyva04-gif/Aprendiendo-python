#importar el random
import random

secret_num = random.randint(1,20) #rango del número secreto
intentos = 0 #variable para contar los intentos

name = input("¿Cuál es tu nombre? ")
print(f"Hi {name}, tendrás que adivinar el número del 1 al 20 que estoy pensando")

while intentos <= 5:
    usernum = int(input("Intenta adivinar: "))

    intentos += 1

    #condiciones para dar pistas
    if usernum < secret_num:
        print("Tu número esta algo bajo")
    
    if usernum > secret_num:
        print("Tu número esta algo alto")

    if usernum > 20:
        print("No exageres")
    
    if usernum == secret_num:
        print("Correcto :)")
        seguir = input("¿Deseas jugar de nuevo? s/n: ") #para reiniciar el loop
        if seguir == "s":
                intentos = 0 #reiniciar el contador de intentos
                secret_num = random.randint(1,20) #y tambien el random
        else: 
            break    

if usernum != secret_num:
        print(f"Te equivocaste, el número secreto era: {secret_num}") #si el user se queda sin intentos
