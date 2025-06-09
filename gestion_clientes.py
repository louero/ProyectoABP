# gestion_clientes.py - Modulo para gestionar clientes en la base de datos SkyRoute.


from conexionDB import conectar

#Menu principal para la gestion de clientes.

def menu_clientes():
    while True:
        print("\n-- GESTIÓN DE CLIENTES --")
        print("1. Ver clientes")
        print("2. Agregar cliente")
        print("3. Buscar cliente")
        print("4. Modificar cliente")
        print("5. eliminar cliente")
        print("6. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ver_clientes()
        elif opcion == "2":
            agregar_cliente()
        elif opcion == "3":
            buscar_cliente_por_cuit()
        elif opcion == "4":
            modificar_cliente()
        elif opcion == "5":
            eliminar_cliente()
        elif opcion == "6":
            break
        else:
            print("Opción no válida")

#Consultar todos los clientes almacenados en la base de datos

def ver_clientes():
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()
        
        if not clientes:
            print("No hay clientes cargados")
        else:
            for cliente in clientes:
                print(f"ID: {cliente[0]}")
                print(f"CUIT: {cliente[1]}")
                print(f"Razón Social: {cliente[2]}")
                print(f"Email: {cliente[3]}")
        conn.close()
    except Exception as e:
        print("error al consultar los clientes:", )

#agregar clientes solicitando los datos por teclado

def agregar_cliente():
    try:
        cuit = input("CUIT del cliente: ")
        razon_social = input("Ingrese Razon social:")
        email = input("Ingrese email:")
    
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO clientes (cuit, razon_social, email) VALUES (%s, %s, %s)", (cuit,razon_social, email ))
        conn.commit()
        conn.close()
    
        print("Cliente agregado correctamente.")
    
    except Exception as e:
        print("error al cargar el cliente")

#buscar cientes por su numero de CUIT ingresandolo por teclado

def buscar_cliente_por_cuit():
    try:
        cuit = input("Ingrese el cuit del cliente: ")
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clientes WHERE cuit = %s", (cuit,))
        cliente = cursor.fetchone()
        if cliente:
            print(f"ID: {cliente[0]} | CUIT: {cliente[1]} | Razón Social: {cliente[2]} | Email: {cliente[3]}")
        else:
            print("Cliente no encontrado.")
        conn.close()
    except Exception as e:
        print("Error al buscar cliente:", e)

#Modificar clientes registrados segun su id_cliente
        
def modificar_cliente():
    id_cliente = input("Ingrese ID del cliente a modificar: ")
    nueva_razon = input("Nueva razón social: ")
    nuevo_cuit = input("Nuevo CUIT: ")
    nuevo_email = input("Nuevo email: ")
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE clientes SET razon_social=%s, cuit=%s, email=%s WHERE id_cliente=%s",
                        (nueva_razon, nuevo_cuit, nuevo_email, id_cliente))
        conn.commit()
        print("Cliente modificado correctamente.")
    except Exception as e:
        print("Error al modificar cliente:", e)
    finally:
        cursor.close()
        conn.close()

#Eliminar clientes de la base de datos segun su id_cliente

def eliminar_cliente():
    id_cliente = input("Ingrese ID del cliente a eliminar: ")
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM clientes WHERE id_cliente=%s", (id_cliente,))
        conn.commit()
        print("Cliente eliminado.")
    except Exception as e:
        print("Error al eliminar cliente:", e)
    finally:
        cursor.close()
        conn.close()
