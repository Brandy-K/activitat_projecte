from fastapi import FastAPI, Depends, HTTPException
from typing import List
from pydantic import BaseModel
from typing import Union
import Alumnat
import alumne
import aula
app = FastAPI()

# Define your Pydantic schema for validation
class Item(BaseModel):
    IdAlumne: int
    IdAula: int
    NomAlumne: str
    Cicle: str
    Curs: str
    Grup: str
    CreatedAt: str
    UpdatedAt: str

# Route to get all students
@app.get("/alumne", response_model=List[Item])
def read_alumne():
    result = Alumnat.read()  # Fetch raw data from the database

    if isinstance(result, dict) and result.get("status") == -1:
        raise HTTPException(status_code=500, detail=result["message"])
    return alumne.alum(result)

# Route to get a student by ID
@app.get("/alumne/{IdAlumne}", response_model=Item)
def read_alumne_by_id(IdAlumne: int):
    result = Alumnat.read_id(IdAlumne)                            

    # Check if there was an error connecting to the database
    if isinstance(result, dict) and result.get("status") == -1:
        raise HTTPException(status_code=500, detail=result["message"])
    elif isinstance(result, dict) and result.get("status") == 0:
        raise HTTPException(status_code=404, detail=result["message"])

    return alumne.alum(result)  # Transform single record into dict

@app.post("/alumne/add")
def add_alumne(new_alumne: Item):
    # Step 1: Check if the classroom (IdAula) exists in the Classroom table
    classroom = aula.read_classroom(new_alumne.IdAula)  # Check if classroom exists
    
    if classroom is None:
        raise HTTPException(status_code=400, detail="Classroom with this IdAula does not exist.")

    # Step 2: Insert the new student into the Alumne table
    result = Alumnat.create_alumne(
        IdAula=new_alumne.IdAula,
        NomAlumne=new_alumne.NomAlumne,
        Cicle=new_alumne.Cicle,
        Curs=new_alumne.Curs,
        Grup=new_alumne.Grup,
        CreatedAt=new_alumne.CreatedAt,
        UpdatedAt=new_alumne.UpdatedAt
    )

    if result:
        return {"status": "success", "message": "New student added successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to add the student to the database.")
