lista_tareas = ["comer", "dormir", "trotar", "estudiar", "trabajar"]

accion = input("ingrese la accion que desee realizar (agregar, ver, actualizar o eliminar): ")

if accion == "agregar":
    print(lista_tareas)
    valor_agregar = input("seleccione tarea a agregar: ")
    lista_tareas.append(valor_agregar)
    print(lista_tareas)
elif accion == "ver":
    print(lista_tareas)
elif accion == "actualizar":
    posicion_actualizar = int(input("Introduzca el registro para actualizar: "))
    print(lista_tareas)
    tarea_actualizar = input("Intruzca tarea para actualizar: ")
    lista_tareas[posicion_actualizar] = (tarea_actualizar)
    print(lista_tareas)
elif accion == "eliminar":
    print(lista_tareas)
    posicion_eliminar = int(input("Introduzca el registro a eliminar: "))
    lista_tareas.pop(posicion_eliminar)
    print(lista_tareas)
else: 
    print("Accion no reconocida, intente de nuevo.")