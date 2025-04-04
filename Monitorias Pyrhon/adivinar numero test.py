import random

universo = random.randint(1, 10)

while True:
    numero = int(input("Ingresa un numero del 1 al 10!: "))
    if numero == universo:
        print("Adivinaste el numero!")
        break
    else:
        print("No lo adivinaste, Intenta de nuevo!")
        print("El numero era: ", universo)