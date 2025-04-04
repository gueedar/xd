while True: 

#variables de operacion
    numero1 = int(input("Ingrese primer numero: "))
    numero2 = int(input("Ingrese segundo numero: "))
    operacion = input("Ingrese que operacion desea realizar ('+', '-', '*', '/', 'prom'): ")

    if operacion == "+": 
        print("El resultado es: ", numero1 + numero2)
    elif operacion == "-":
        print("El resultado es: ", numero1 - numero2)
    elif operacion == "*":
        print("El resultado es: ", numero1 * numero2)
    elif operacion == "/":
        if numero2 != 0:
            print("El resultado es: ", numero1 / numero2)
        else:
            print("Division por '0' no es valida")
    elif operacion == "prom":
        numero3 = int(input("ingrese 3er numero: "))
        print("El resultado es: ", (numero1 + numero2 + numero3) / 3)
    else:
        print("operacion no valida")

    cerrar = input("digite '0' si desea continuar, de lo contrario presione cualquier otra tecla: ")
    if cerrar == "0":
        print("programa finalizado")
        break