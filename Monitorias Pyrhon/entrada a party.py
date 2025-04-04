edad = int(input("Digite su edad: "))

if edad < 18:
    print("Usted es menor de edad")

invitacion = input("¿Tiene invitacion especial? (digite 'si' si es el caso, de lo contrario digite 'no' ): ")

if edad < 18 and invitacion == "no":
    print("Usted no puede entrar")
elif edad > 18 or invitacion == "no" or invitacion == "si":
    print("Usted puede ingresar")