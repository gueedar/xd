libros = ["manual", "diccionario", "biblia", "100 años de soledad", "don quijote"]

accion = input("Selecione accion a realizar (agregar, ver, actualizar o eliminar): ")

if accion == "agregar":
    print(libros)
    agregar_libro = input("Digite libro a agregar: ")
    libros.append(agregar_libro)
    print(libros)
elif accion == "ver":
    print(libros)
elif accion == "actualizar":
    print(libros)
    registro_actualziar = int(input("Ingrese registro a actualizar: "))
    actualizar_libro = input("Ingrese libro a actualizar: ")
    libros[registro_actualziar] = (actualizar_libro)
    print(libros)
elif accion == "eliminar":
    print(libros)
    registro_eliminar = int(input("Introduzca registro a eliminar: "))
    libros.pop(registro_eliminar)
    print(libros)
else: 
    print("Accion no reconocida, intendelo de nuevo.")