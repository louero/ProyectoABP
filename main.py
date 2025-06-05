#SkyRoute - sistema de Gestion de pasajes Aereos
#Evidencia 2 modulo programador

#Desarrollado por: GRUPO N19  Nombre de grupo: GRupo 9
# Fiorio Fuenzalida Tadiana Alejandra -Tello Pablo Andrés
# Eroles Prado Cecilia Lourdes - Gómez Álvarez Julieta - 


#CONTROLAR


#para modularizar
from gestion_clientes import menu_clientes
from gestion_destinos import menu_destinos
from gestion_ventas import menu_ventas, consultar_ventas, boton_arrepentimiento

while True:
    print("Bienvenido a SkyRoute - Sistema de gestión de pasajes")
    print("¿Que desea hacer?")
    print("1. Gestionar Clientes")
    print("2. Gestionar Destinos")
    print("3. Gestionar Ventas")
    print("4. Consultar Ventas")
    print("5. Boton de arrepentimiento")
    print("6. Reporte general")
    print("7. Acerca del sistema")
    print("8. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        menu_clientes()
    elif opcion == "2":
        menu_destinos()
    elif opcion == "3":
        menu_ventas()
    elif opcion == "4":
        print("¿que tipo de venta desea consultar?")
        print("1. Activas")
        print("2. canceladas/anuladas")
        tipo = input("seleccione una opcion: ")
        
        if tipo == "1":
            consultar_ventas("Activa")
        elif tipo == "2":
            consultar_ventas("anulada")
    elif opcion == "5":
        boton_arrepentimiento()
    elif opcion == "6":
        print("ver reporte general (cargando...)")
    elif opcion == "8":
        print("Gracias por usar Skyroute")
        break
    else:
        print("Opción inválida.")
