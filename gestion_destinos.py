#Apartado para gestion_destinos.py Modulo para gestionar destinos en la base de datos SkyRoute.


from conexionDB import conectar

def menu_destinos():
    while True:
        print("GESTIÓN DE DESTINOS --")
        print("1. Ver destinos")
        print("2. Agregar destinos")
        print("3. Buscar destino por ciudad")
        print("4. Modificar destino")
        print("5. Eliminar destino")
        print("6. Volver al menu principal")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ver_destinos()
        elif opcion == "2":
            agregar_destino()
        elif opcion == "3":
            buscar_destino_por_ciudad()
        elif opcion == "4":
            modificar_destino()
        elif opcion == "5":
            eliminar_destino()
        elif opcion == "6":
            break
        else:
            print("Opción no válida")


#ver todos los destinos 

def ver_destinos():
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM destinos")
        destinos = cursor.fetchall()
        
        if not destinos:
            print("No hay destinos cargados.")
        else:
            for destino in destinos:
                print(f"ID: {destino[0]}, Ciudad: {destino[1]}, País: {destino[2]}, Costo base: ${destino[3]}")
        
        conn.close()
    except Exception as e:
        print("Error al consultar los destinos:", e)


def agregar_destino():
    try:
        ciudad = input("Ingrese ciudad: ")
        pais = input("Ingrese país: ")
        costo = float(input("Ingrese costo base: "))

        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO destinos (ciudad, pais, costo_base) VALUES (%s, %s, %s)", (ciudad, pais, costo))
        conn.commit()
        conn.close()

        print("Destino agregado correctamente.")
    except Exception as e:
        print("Error al agregar el destino:", e)

# buscar destino por ciudad

def buscar_destino_por_ciudad():
    ciudad = input("Ingrese la ciudad: ")
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM destinos WHERE ciudad = %s", (ciudad,))
        destino= cursor.fetchone()
        
        if destino:
            print(f"ID: {destino[0]} | Ciudad: {destino[1]} | País: {destino[2]} | Costo: ${destino[3]:,.2f}")
        else:
            print("Destino no encontrado.")
    
        conn.close()
    except Exception as e:
        print("Error al buscar destino:", e)



#modificar destino

def modificar_destino():
    try:
        id_destino = input("Ingrese el ID del destino a modificar: ")
        nueva_ciudad = input("Nueva ciudad: ")
        nuevo_pais = input("Nuevo país: ")
        nuevo_costo = float(input("Nuevo costo base: "))

        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE destinos
            SET ciudad = %s, pais = %s, costo_base = %s
            WHERE id_destino = %s
        """, (nueva_ciudad, nuevo_pais, nuevo_costo, id_destino))
        conn.commit()
        conn.close()

        print("Destino modificado con éxito.")
    except Exception as e:
        print("Error al modificar destino:", e)

#eliminar destino

def eliminar_destino():
    try:
        id_destino = input("Ingrese el ID del destino a eliminar: ")

        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM destinos WHERE id_destino = %s", (id_destino,))
        conn.commit()
        conn.close()

        print("Destino eliminado.")
    except Exception as e:
        print("Error al eliminar destino:", e)