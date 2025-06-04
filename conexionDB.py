import mysql.connector

def conectar():
    conexion = mysql.connector.connect(
        host="localhost",
        user="user",         #
        password="password",  # La contraseña de mySQL
        database="skyrouteDB"
    )
    return conexion

