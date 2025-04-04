contactos = {
    "Maria" : "3258964710",
    "Oscar" : "3827648231",
    "David" : "3658794525"
}

print(contactos)
accion = input("Ingrese accion a realizar (agregar, editar o eliminar): ")

if accion == "agregar":
    print(contactos)
    usuario = input("Ingrese nombre del usuario a agregar: ")
    numero = int(input("Ingrese el numero del nuevo usuario: "))
    contactos[usuario] = numero
    print("Usuario agregado con exito!")
    print(contactos)
elif accion == "editar":
    print(contactos)
    usuario_editar = input("Seleccione valor a editar (nombre o numero): ")
    if usuario_editar == "nombre":
        print(contactos)
        clave_editar_nombre = input("Introduca el nombre del usuario que quiere editar: ")
        nuevo_nombre = input("Ingrese el nuevo nombre de usuario: ")
        contactos[nuevo_nombre] = contactos.pop(clave_editar_nombre)
        print("Nombre de usuario editado con exito!")
        print(contactos)
    elif usuario_editar == "numero":
        print(contactos)
        clave_editar_numero = input("Digite el nombre del usuario al cual editara su numero: ")
        nuevo_numero = int(input("Digite nuevo numero: "))
        contactos[clave_editar_numero] = nuevo_numero
        print("Numero editado con exito!")
        print(contactos)
    else:
        print("Accion no reconocida, intente de nuevo")
elif accion == "eliminar":
    print(contactos)
    clave_usuario_eliminar = input("Ingrese el nombre del usuario que desea eliminar: ")
    print(f"esta seguro que desea eliminar a {clave_usuario_eliminar}?")
    decicion = input("('si - no'): ")
    if decicion == "si":
        del contactos[clave_usuario_eliminar]
        print("El usuario ha sido eliminardo con exito!")
        print(contactos)
    elif decicion == "no":
        print("Accion cancelada")
    else:
        print("accion no reconocida, intente de nuevo")
else:
    print("accion no reconocida, intente de nuevo")