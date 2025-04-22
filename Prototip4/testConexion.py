import mysql.connector
from mysql.connector import Error

def establish_connection():
    """Establece la conexión a la base de datos y la retorna."""
    try:
        connection = mysql.connector.connect(
            host='localhost',       # Cambia esto si tu servidor no está en localhost
            user='root',            # Reemplaza con tu usuario de MySQL
            password='root',        # Reemplaza con tu contraseña de MySQL
            database='tapatapp'     # Reemplaza con el nombre de tu base de datos
        )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
            return connection
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def get_all_users(connection):
    """Ejecuta una consulta en la base de datos usando la conexión proporcionada."""
    try:
        cursor = connection.cursor()
        query = "SELECT * FROM User"
        cursor.execute(query)

        # Obtener y mostrar los resultados
        results = cursor.fetchall()
        for row in results:
            print(row)
    except Error as e:
        print(f"Error al ejecutar la consulta: {e}")

def connect_and_query():
    """Función principal que conecta a la base de datos y ejecuta la consulta."""
    connection = establish_connection()
    if connection:
        try:
            get_all_users(connection)
        finally:
            connection.close()
            print("Conexión cerrada")

# Llamar a la función principal
connect_and_query()

# pip install mysql-connector-python
# pip show mysql-connector-python
