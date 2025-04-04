nombre = ["David", "Andres", "Nicolas", "Eric", "Felipe", "kevin", "Sebastian"]

edad = [15, 18, 17, 18, 17, 16, 16]

accion = input("Introduzca accion a realizar (agregar, ver, actualizar o eliminar): ")

if accion == "agregar":
    nombre_agregar = input("Introduzca nombre a agregar: ")
    edad_agregar = int(input("Introduzca edad a agregar: "))
    nombre.append(nombre_agregar)
    edad.append(edad_agregar)
    print(nombre)
    print(edad)
elif accion == "ver":
    nombre.extend(edad)
    print(nombre)
elif accion == "actualizar":
    lista_actualizar = input("Seleccione registro a actualizar (nombre, edad): ")
    if lista_actualizar == "nombre":
        print(nombre)
        registro_nombre_actualizar = int(input("Ingrese registro a actualizar: "))
        nombre_actualizar = input("Ingrese nombre a actualizar: ")
        nombre[registro_nombre_actualizar] = (nombre_actualizar)
        print(nombre)
    elif lista_actualizar == "edad":
        print(edad)
        registro_edad_actualizar = int(input("Ingrese registro a actualizar: "))
        edad_actualizar = input("Ingrese edad a actualizar: ")
        edad[registro_edad_actualizar] = (edad_actualizar)
        print(edad)
elif accion == "eliminar":
    lista_eliminar = input("Seleccione registro a manipular (nombre o edad): ")
    if lista_eliminar == "nombre":
        print(nombre)
        registro_nombre_eliminar = int(input("Ingrese registro a eliminar: "))
        nombre.pop(registro_nombre_eliminar)
        print(nombre)
    elif lista_eliminar == "edad":
        print(edad)
        registro_edad_eliminar = int(input("Ingrese registro a eliminar: "))
        edad.pop(registro_edad_eliminar)
        print(edad)
else:
    print("Accion no reconocida, intente de nuevo.")