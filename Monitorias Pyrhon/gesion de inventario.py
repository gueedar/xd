productos = {
    "tomate" : "5000",
    "frijoles" : "8000",
    "arroz" : "6000",
    "carne" : "10000"
}

print("Bienvenido al sistema de gestion de inventario del supermarket!")
accion = input("Ingrese la accion que desea realizar (agregar o consultar): ")

if accion == "agregar":
    print(productos)
    nuevo_producto = input("Ingrese el nombre del nuevo producto: ")
    nuevo_precio = int(input("Ingrese el precio de este nuevo producto: "))
    productos[nuevo_producto] = nuevo_precio
    print("Nuevo producto agregado con exito!")
    print(productos)
elif accion == "consultar":
    print(productos)
    producto_consultar = input("ingrese el nombre del producto que desea consultar: ")
    print(f"el precio del producto {producto_consultar} es:")
    print(productos[producto_consultar])
else: 
    print("No se reconocio la accion, intente de nuevo.") 