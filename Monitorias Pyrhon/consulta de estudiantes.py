estudiantes = {
    "andres" : 90,
    "david" : 92,
    "nicol" : 30,
    "andrea" : 60,
    "matias" : 86
}

print("Bienvenido a el sistema de consulta de estudiantes.")
accion = input("Seleccione la accion a realizar (agregar, consultar o mostrar): ")

if accion == "agregar":
    nuevo_nombre = input("Digite el nombre del nuevo estudiante: ")
    nueva_calificacion = int(input(f"Ingrese la calificacion del estudiante {nuevo_nombre}: "))
    estudiantes[nuevo_nombre] = nueva_calificacion
    print("Estudiante registrado con exito!")
    print(estudiantes)
elif accion == "consultar":
    print("Lista de estudiantes: ")
    for estudiante in estudiantes.keys():
        print(estudiante)
    nombre_estudiante_consultar = input("seleccione el nombre del estudiante que desea consultar: ")
    print(f"La calificacion del estudiante {nombre_estudiante_consultar} es:")
    print(estudiantes[nombre_estudiante_consultar])
elif accion == "mostrar":
    print("Las calificaciones son: ")
    for calificaciones in estudiantes.values():
        print(calificaciones)
else:
    print("Accion no reconocida, intente de nuevo")