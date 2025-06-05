import mysql.connector

def conectar():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",         #
        password="465415lu*",  # La contraseña de mySQL
        database="skyrouteDB"
    )
    return conexion

