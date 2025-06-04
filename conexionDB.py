import mysql.connector

def conectar():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",         # Por ejemplo: root
        password="465415lu*",  # La que configuraste al instalar MySQL
        database="skyrouteDB"
    )
    return conexion

