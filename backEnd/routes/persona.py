from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

persona = APIRouter()
personas = []

class model_personas(BaseModel):
    id: str
    nombre: str
    primer_apellido: str
    segundo_apellido: Optional[str]
    edad: int
    fecha_nacimiento: datetime
    curp: str
    tipo_sangre: str
    create_at: datetime = datetime.now()
    estatus: bool = False

@persona.get('/')
def bienvenida():
    return "Bienvenida al sistema"

@persona.get('/personas')
def get_personas():
    return personas

@persona.post('/personas')
def save_personas(datos_persona: model_personas):
    personas.append(datos_persona)
    return "Datos guardado correctamente"

@persona.delete('/personas/{persona_id}')
def delete_persona(persona_id: str):
    for index, persona in enumerate(personas):
        if persona.id == persona_id:
            del personas[index]
            return "Persona eliminada correctamente"
    raise HTTPException(status_code=404, detail="Persona no encontrada")

@persona.put('/personas/{persona_id}')
def update_persona(persona_id: str, datos_actualizados: model_personas):
    for index, persona in enumerate(personas):
        if persona.id == persona_id:
            personas[index] = datos_actualizados
            return "Datos actualizados correctamente"
    raise HTTPException(status_code=404, detail="Persona no encontrada")

@persona.get('/personas/{persona_id}')
def get_persona(persona_id: str):
    for persona in personas:
        if persona.id == persona_id:
            return persona
    raise HTTPException(status_code=404, detail="Persona no encontrada")