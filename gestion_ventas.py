#Apartado para gestion_ventas.py Modulo para gestionar ventas en la base de datos SkyRoute.



from conexionDB import conectar
import datetime

def menu_ventas():
    while True:
        print("GESTIÓN DE VENTAS --")
        print("1. Ver ventas")
        print("2. Registrar venta")
        print("3. Modificar venta")
        print("4. Eliminar venta")
        print("5. Botón de arrepentimiento")
        print("6. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")


        if opcion == "1":
            ver_ventas()
        elif opcion == "2":
            registrar_venta()
        elif opcion == "3":
            modificar_venta()
        elif opcion == "4":
            eliminar_venta()
        elif opcion == "5":
            boton_arrepentimiento()
        elif opcion == "6":
            break
        else:
            print("Opción no válida.")

#Ver todas las ventas
def ver_ventas():
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ventas")
        ventas = cursor.fetchall()

        if ventas:
            for venta in ventas:
                print(f"ID: {venta[0]}, Cliente: {venta[1]}, Destino: {venta[2]}, Fecha: {venta[3]}, Costo: ${venta[4]}, Estado: {venta[5]}")
        else:
            print("No hay ventas registradas.")
        
        conn.close()
    except Exception as e:
        print("Error al ver ventas:", e)

#Consultar ventas segun su estado: (DESDE main.py)

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



#Registrar venta 

def registrar_venta():
    try:
        id_cliente = input("ID del cliente: ") 
        id_destino = input("ID del destino: ")
        costo_total = float(input("costo total: "))
        
        conn = conectar()
        cursor = conn.cursor()
        
# Verifica si el cliente existe
        cursor.execute("SELECT * FROM clientes WHERE id_cliente = %s", (id_cliente,))
        if not cursor.fetchone():
            print("⚠️ El cliente con ese ID no existe.")
            conn.close()
            return        
        
# Verifica si el destino existe
        cursor.execute("SELECT * FROM destinos WHERE id_destino = %s", (id_destino,))
        if not cursor.fetchone():
            print("⚠️ El destino con ese ID no existe.")
            conn.close()
            return        

#si todo existe, entonces puede registrar la venta        
        
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
























#modificar una venta

def modificar_venta():
    try:
        id_venta = input("ID de la venta a modificar: ")
        nuevo_cliente = input("Nuevo ID cliente: ")
        nuevo_destino = input("Nuevo ID destino: ")
        nuevo_costo = float(input("Nuevo costo total: "))

        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE ventas
            SET id_cliente = %s, id_destino = %s, costo_total = %s
            WHERE id_venta = %s
        """, (nuevo_cliente, nuevo_destino, nuevo_costo, id_venta))
        conn.commit()
        print("Venta modificada correctamente.")
        conn.close()
    except Exception as e:
        print("Error al modificar la venta:", e)

#eliminar una venta

def eliminar_venta():
    try:
        id_venta = input("ID de la venta a eliminar: ")
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM ventas WHERE id_venta = %s", (id_venta,))
        conn.commit()
        print("Venta eliminada.")
        conn.close()
    except Exception as e:
        print("Error al eliminar la venta:", e)
        
#Boton de arrepentimiento
                
def boton_arrepentimiento():
    try:
        id_venta = input("ID de la venta a anular: ")

        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT fecha_venta, estado_venta FROM ventas WHERE id_venta = %s", (id_venta,))
        resultado = cursor.fetchone()

        if resultado:
            fecha_venta, estado = resultado
            if estado == 'Anulada':
                print("La venta ya está anulada.")
                return
            
            ahora = datetime.datetime.now()
            diferencia = ahora - fecha_venta

            if diferencia.total_seconds() <= 300:  # dentro de los 5 minutos
                cursor.execute("""
                    UPDATE ventas
                    SET estado_venta = 'Anulada', fecha_anulacion = %s
                    WHERE id_venta = %s
                """, (ahora, id_venta))
                conn.commit()
                print("Venta anulada con éxito.")
            else:
                print("No se puede anular: pasaron más de 5 minutos.")
        else:
            print("No se encontró una venta activa con ese ID.")

        conn.close()
    except Exception as e:
        print("Error al anular la venta:", e)
