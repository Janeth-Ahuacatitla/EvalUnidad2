from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
from typing import Optional


persona = APIRouter()
personas=[]

class model_personas(BaseModel):
    id:int
    nombre:str
    primer_apellido: str
    segundo_apellido: Optional[str]
    edad: int
    fecha_nacimiento: datetime
    curp: str
    tipo_sangre: str
    created_at: datetime = datetime.now()
    estatus: bool = False


@persona.get ('/')

def bienvenida():
    return "Bienvenido al API del sistema"

@persona.get("/personas")

def get_personas():
    return personas

@persona.post('/personas')

def save_personas(datos_persona:model_personas):
    personas.append(datos_persona)
    return "Datos guardados correctamente"


@persona.put('/personas/{persona_id}')
def update_persona(persona_id: int, updated_persona: model_personas):
    for index, persona in enumerate(personas):
        if persona.id == persona_id:
            personas[index] = updated_persona
            return "Datos actualizados correctamente"
    raise HTTPException(status_code=404, detail="Persona no encontrada")

@persona.delete('/personas/{persona_id}')
def delete_persona(persona_id: int):
    for index, persona in enumerate(personas):
        if persona.id == persona_id:
            del personas[index]
            return "Datos eliminados correctamente"
    raise HTTPException(status_code=404, detail="Persona no encontrada")