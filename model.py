import mysql.connector
from mysql.connector import Error

def db_model():
    try:
        dbname = "alumnat"
        user = "root"
        password = "password"
        host = "localhost"
        port = "3306"
        charset = "utf8mb4"

        # Try to establish a connection
        conn = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=dbname,
            charset=charset
        )

        # Check if the connection was successful
        if conn.is_connected():
            return conn
        else:
            return {"status": -1, "message": "Failed to connect to the database"}

    except Error as e:
        # Catch any connection-related errors and return a detailed message
        return {"status": -1, "message": f"Error de connexió: {str(e)}"}
