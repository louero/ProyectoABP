# test_conexion.py
from conexionDB import conectar

try:
    conn = conectar()
    if conn.is_connected():
        print("se pudooooo.")
    conn.close()
except Exception as e:
    print("Error al conectar:", e)
