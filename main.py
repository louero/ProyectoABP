



from gestion_clientes import menu_clientes
from gestion_destinos import menu_destinos
from gestion_ventas import menu_ventas

while True:
    print("\nBienvenido a SkyRoute - Sistema de gestión de pasajes")
    print("1. Gestionar Clientes")
    print("2. Gestionar Destinos")
    print("3. Gestionar Ventas")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        menu_clientes()
    elif opcion == "2":
        menu_destinos()
    elif opcion == "3":
        menu_ventas()
    elif opcion == "4":
        print("Gracias por usar SkyRoute.")
        break
    else:
        print("Opción inválida.")
