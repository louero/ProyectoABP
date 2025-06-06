# controlar conexion
from conexionDB import conectar

try:
    conn = conectar()
    if conn.is_connected():
        print("se pudooooo.") #modificar esto ajaja
    conn.close()
except Exception as e:
    print("noo se pudo:", e) #modificar esto ajaja
