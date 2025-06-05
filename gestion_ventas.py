#Apartado para geston de ventas


from conexionDB import conectar
import datetime

def menu_ventas():
    while True:
        print("GESTIÓN DE VENTAS --")
        print("1. Registrar venta")
        print("2. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_venta()
        elif opcion == "2":
            break
        else:
            print("Opción no válida")

def registrar_venta():
    try:
        id_cliente = input("ID del cliente: ") 
        id_destino = input("ID del destino: ")
        costo_total = float(input("costo total: "))
        
        conn = conectar()
        cursor = conn.cursor()
        
        fecha_actual = datetime.datetime.now()
        estado = "Activa"
        
        cursor.execute("""
            INSERT INTO ventas (id_cliente, id_destino, fecha_venta, costo_total, estado_venta)
            VALUES (%s, %s, %s, %s, %s)
        """, (id_cliente, id_destino, fecha_actual, costo_total, estado))
        
        conn.commit()
        conn.close()

        print("Venta registrada con éxito.")
    except Exception as e:
        print("Error al registrar venta:", e)


def consultar_ventas(estado):
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ventas WHERE estado_venta = %s", (estado,))
        ventas = cursor.fetchall()
        
        if not ventas:
            print(f"No hay ventas con estado {estado}")
        else:
            for venta in ventas:
                print(f"ID: {venta[0]}, Cliente: {venta[1]}, Destino: {venta[2]}, Fecha: {venta[3]}, Costo: ${venta[4]}, Estado: {venta[5]}")
        conn.close()
    except Exception as e:
        print("Error al consultar ventas:", e)


def boton_arrepentimiento():
    try:
        id_venta = input("Ingrese el ID de la venta a anular: ")

        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT fecha_venta FROM ventas WHERE id_venta = %s AND estado_venta = 'Activa'", (id_venta,))
        resultado = cursor.fetchone()

        if resultado:
            fecha_venta = resultado[0]
            ahora = datetime.datetime.now()
            diferencia = ahora - fecha_venta

            if diferencia.total_seconds() <= 300:  #5 MINUTOS HAY QUE VER ESTO
                cursor.execute("""
                    UPDATE ventas
                    SET estado_venta = 'Anulada', fecha_anulacion = %s
                    WHERE id_venta = %s
                """, (ahora, id_venta))
                conn.commit()
                print("Venta anulada con éxito.")
            else:
                print("No se puede anular: pasaron más de 5 minutos.") #modificar el tiempo no me acuerdo cuanto era
        else:
            print("No se encontró una venta activa con ese ID.")
        
        conn.close()
    except Exception as e:
        print("Error al anular la venta:", e)