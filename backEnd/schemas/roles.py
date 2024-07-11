from typing import List, Union
from pydantic import BaseModel
from datetime import datetime

class RolesBase(BaseModel):
    Descripcion: str
    Nombre: str
    Estatus: bool
    Fecha_Registro: datetime
    Fecha_Actualizacion: datetime

class RolesCreate(RolesBase):
    pass

class RolesUpdate(RolesBase):
    pass

class Roles(RolesBase):
    id: int
    #owner_id: int clave foranea
    class Config:
        orm_mode = True


   