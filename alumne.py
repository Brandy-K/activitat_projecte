from model import db_model  # Assuming this connects to the database


# Function to transform a single database row into a dictionary
def alum(item) -> dict:
    return {
        "IdAlumne": item[0],
        "IdAula": item[1],
        "NomAlumne": item[2],
        "Cicle": item[3],
        "Curs": item[4],
        "Grup": item[5],
        "CreatedAt": item[6],
        "UpdatedAt": item[7],
    }


# Function to transform a list of database rows into a list of dictionaries
def alum(alumne_list) -> list:
    return [alum(alumna) for alumna in alumne_list]


# Function to add a new student (alumne) to the database
def AlumneCreate(IdAula: int, NomAlumne: str, Cicle: str, Curs: str, Grup: str, CreatedAt: str, UpdatedAt: str):
    try:
        conn = db_model()  # Connect to the database
        cur = conn.cursor()

        # SQL query to insert a new alumne
        query = """
        INSERT INTO alumne (IdAula, NomAlumne, Cicle, Curs, Grup, CreatedAt, UpdatedAt)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (IdAula, NomAlumne, Cicle, Curs, Grup, CreatedAt, UpdatedAt)

        cur.execute(query, values)
        conn.commit()  # Save changes to the database
        conn.close()

        return True  # Return True if the insert was successful

    except Exception as e:
        print(f"Error inserting new alumne: {e}")
        return False  # Return False if there was an error
