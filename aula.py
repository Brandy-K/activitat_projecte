from model import db_model

# Function to check if the classroom exists
def read_classroom(IdAula: int):
    try:
        conn = db_model()
        cur = conn.cursor()
        query = "SELECT * FROM aula WHERE IdAula = %s"
        cur.execute(query, (IdAula,))
        classroom = cur.fetchone()
        conn.close()
        
        # Return the classroom if found, None otherwise
        return classroom
    
    except Exception as e:
        print(f"Error reading classroom: {e}")
        return None

# Function to insert a new classroom if necessary
def create_classroom(IdAula: int, DescAula: str):
    try:
        conn = db_model()
        cur = conn.cursor()
        query = "INSERT INTO classroom (IdAula, DescAula, ...) VALUES (%s, %s, ...)"
        values = (IdAula, DescAula["DescAula"], ...)
        cur.execute(query, values)
        conn.commit()
        conn.close()
        
        return True
    
    except Exception as e:
        print(f"Error creating classroom: {e}")
        return False
