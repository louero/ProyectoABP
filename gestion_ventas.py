#cambiar gestion clientes por ventas


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
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes")
    for cliente in cursor.fetchall():
        print(cliente)
    conn.close()

def agregar_cliente():
    nombre = input("Nombre del cliente: ")
    cuit = input("CUIT del cliente: ")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clientes (nombre, cuit) VALUES (%s, %s)", (nombre, cuit))
    conn.commit()
    conn.close()
    print("Cliente agregado correctamente.")
