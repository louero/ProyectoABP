#Apartado para geston de clientes
#CONTROLAR

from conexionDB import conectar

def menu_clientes():
    while True:
        print("\n-- GESTIÓN DE CLIENTES --")
        print("1. Ver clientes")
        print("2. Agregar cliente")
        print("3. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ver_clientes()
        elif opcion == "2":
            agregar_cliente()
        elif opcion == "3":
            break
        else:
            print("Opción no válida")

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
