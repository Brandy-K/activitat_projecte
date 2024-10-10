from model import db_model

def read():
    conn = db_model()

    # Check if the connection failed and return an error message
    if isinstance(conn, dict) and conn.get("status") == -1:
        return conn

    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM alumne")
        items = cur.fetchall()

    except Exception as e:
        return {"status": -1, "message": f"Error executing query: {e}"}

    finally:
        conn.close()

    return items  # Return the fetched items


def read_id(IdAlumne):
    conn = db_model()

    # Check if the connection failed and return an error message
    if isinstance(conn, dict) and conn.get("status") == -1:
        return conn

    try:
        cur = conn.cursor()
        query = "SELECT * FROM alumne WHERE IdAlumne = %s"
        value = (IdAlumne,)
        cur.execute(query, value)

        item = cur.fetchone()

    except Exception as e:
        return {"status": -1, "message": f"Error executing query: {e}"}

    finally:
        conn.close()

    # Return the fetched item or a message if no item was found
    if item:
        return item
    else:
        return {"status": 0, "message": "No record found for the given ID"}
