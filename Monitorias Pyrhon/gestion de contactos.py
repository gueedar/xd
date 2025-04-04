contactos = {"Andres":321654897, "Sofia":987654321, "David":654987321, "Karen":654321987}

accion = input("Seleccione accion a realizar (agregar, buscar o listar): ")

def agregar():
    nombre = input("Ingrese nombre del nuevo contacto: ")
    numero = int(input("Ingrese numero del contacto nuevo: "))
    contactos[nombre] = numero
    print("El usuario se agrego exitosamente!")
    print(contactos)

def buscar():
    indice = input("Ingrese el elemento por el cual desea buscar (nombre o numero): ")
    if indice == "nombre":
        nombre = input("Ingrese el nombre que desea buscar: ")
        print("Contacto encontrado con exito!")
        print(nombre, contactos[nombre])
    elif indice == "numero":
        numero = int(input("Ingrese el numero que desea buscar: "))
        clave_encontrada = None
        for clave, valor in contactos.items():
            if valor == numero:
                clave_encontrada = clave
                break
        if clave_encontrada:
            print("Felicidades! usuario encontrado: ")
            print(f"El contacto con el numero {numero} es {clave_encontrada}.")
        else: 
            print("Contacto no encontrado, intente de nuevo.")
    else:
        print("acción no identificada, intente de nuevo.")

def listar():
    print("Estos son los contactos actuales: ")
    print(contactos)

if accion == "agregar":
    agregar()
elif accion == "buscar":
    buscar()
elif accion == "listar":
    listar()
else:
    print("Accion no encontrada, intente de nuevo.")