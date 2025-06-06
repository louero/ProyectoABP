#conexionDB.py - mySQL con python
#se instalo con pip install mysql-connector-python desde "terminal"


import mysql.connector
from config import host, user, password, database #importa datos desde config.py (no necesito llenar campos)

def conectar():
    conexion = mysql.connector.connect(
        host=host,
        user=user,         
        password=password,  
        database=database
    )
    return conexion

