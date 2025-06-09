# ProyectoABP
Evidencias de aprendizajes N° 3 Módulo: Programador PROYECTO (ABP) 

Nombre del proyecto y descripción.

"SkyRoute – Sistema de Gestión de Pasajes Aéreos"
Para este proyecto se busca implementar un sistema digital básico que permita 
-Registrar, modificar, eliminar y consultar clientes, destinos y ventas.
-Gestionar las ventas activas o anuladas.
-Anular ventas realizadas recientemente (función "Botón de arrepentimiento").

Se desarrolla en Python con conexión a base de datos MySQL.


Integrantes con nombre + usuario GitHub:

-Fiorio Fuenzalida Tadiana Alejandra - GitHub: @TadianaFiorio
-Tello Pablo Andrés - GitHub: @PabloAndresTello
-Eroles Prado Cecilia Lourdes - GitHub: @louero
-Gómez Álvarez Julieta - GitHub: @JulietaGomez99


Instrucciones para ejecutar el sistema.

Requisitos:
-python 3
-MySQL 
Libreria mysql-connector-python e instalar pip install mysql-connector-python por terminal.

-Descargar o clonar el repositorio desde GitHub.

-Importar el archivo skyrouteDB.sql en tu gestor de base de datos MySQL.

-Configurar tus credenciales en conexionDB.py o config.py:

host = 'localhost'
user = 'root'
password = 'contraseña personal'
database = 'skyrouteDB'

Ejecutar test_conexion.py para comprobar que la base de datos esté conectada.
Si todo funciona, ejecutar main.py para comenzar a usar el sistema desde consola.

Lista completa de archivos y carpetas del repositorio.

-README.md               # Informacion general del proyecto
-ConexionDB.py           # Conexión a MySQL
-config.py               # Datos de conexión
-gestion_clientes.py     # CRUD de clientes
-gestion_destinos.py     # CRUD de destinos
-gestion_ventas.py       # CRUD de ventas
-main.py                 # Menu principal del sistema
-skyrouteDB.sql          # Script SQL para crear y cargar la BDD
-test_conexion.py        # Verifica que haya conexión a MySQL


Funcionalidades principales:

-clientes: ver, agregar, buscar por CUIT, modificar, eliminar.

-Destinos: ver, agregar, buscar por ciudad, modificar, eliminar.

-Ventas: ver todas, registrar, modificar, eliminar, anular (dentro de 5 minutos)

-Consultas por estado: consultar ventas activas o anuladas.


NOTA GRUPAL: 
 


