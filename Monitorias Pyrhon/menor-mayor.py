numero1 = int(input("Ingrese primer numero: "))

numero2 = int(input("Ingrese segundo numero: "))

if numero1 == numero2:
    print("Los numeros son iguales")
elif numero1 > numero2:
    print("El numero ", numero1, "es mayor que", numero2)
elif numero1 < numero2:
    print("El numero ", numero1, "es menor que ", numero2)
else: 
    print("Numero no registrado")
    