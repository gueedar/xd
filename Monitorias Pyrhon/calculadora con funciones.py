numero1 = int(input("Ingrese un numero: "))

numero2 = int(input("Ingrese otro numero: "))

operacion = input("Digite que operacion dese realizar (+, -, *, /): ")

def division():
    print(f"El resultado de la operacion es: {numero1 / numero2}")

def multiplicacion():
    print(f"El resultado de la operacion es: {numero1 * numero2}")

def suma():
    print(f"El resultado de la operacion es: {numero1 + numero2}")

def resta():
    print(f"El resultado de la operacion es: {numero1 - numero2}")

if operacion == "/":
    division()
elif operacion == "*":
    multiplicacion()
elif operacion == "+":
    suma()
elif operacion == "-":
    resta()
else:
    print("Operacion no reconocida, por favor intente de nuevo")