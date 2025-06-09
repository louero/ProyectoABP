# controlar conexion SQL-Python
from conexionDB import conectar

try:
    conn = conectar()
    if conn.is_connected():
        print("conexion exitosa.") 
    conn.close()
except Exception as e:
    print("No se pudo realizar la conexion", e) 
