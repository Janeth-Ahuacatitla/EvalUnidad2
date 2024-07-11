from fastapi import APIRouter, HTTPException, Depends, Request
from sqlalchemy.orm import Session
import crud.roles, config.db, schemas.roles, models.roles
from typing import List

rol = APIRouter()

models.roles.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@rol.get("/roles/", response_model=List[schemas.roles.Roles], tags=["roles"])
def read_rol(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_roles= crud.roles.get_roles(db=db, skip=skip, limit=limit)
    return db_roles

@rol.post("/roles/{id}", response_model=schemas.roles.Roles, tags=["roles"])
def read_rol(id: int, db: Session = Depends(get_db)):
    db_roles= crud.roles.get_roles(db=db, id=id)
    if db_roles is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_roles

@rol.post("/roles/", response_model=schemas.roles.Roles, tags=["Roles"])
def create_rol(rol: schemas.roles.RolesCreate, db: Session = Depends(get_db)):
    db_roles = crud.roles.get_rol_by_nombre(db, rol=rol.Nombre)
    if db_person:
        raise HTTPException(status_code=400, detail="Usuario existente intenta nuevamente")
    return crud.persons.create_person(db=db, person=person)

@rol.put("/roles/{id}", response_model=schemas.roles.Roles, tags=["roles"])
def update_Roles(id: int, rol: schemas.roles.RolesUpdate, db: Session = Depends(get_db)):
    db_roles = crud.roles.update_roles(db=db, id=id, rol=rol)
    if db_roles is None:
        raise HTTPException(status_code=404, detail="Usuario no existe, no actualizado")
    return db_roles

@rol.delete("/roles/{id}", response_model=schemas.roles.Roles, tags=["Roles"])
def delete_roles(id: int, db: Session = Depends(get_db)):
    db_roles = crud.roles.delete_rol(db=db, id=id)
    if db_roles is None:
        raise HTTPException(status_code=404, detail="Usuario no existe, no se pudo eliminar")
    return db_roles

# @user.post("/login",tags=['autenticacion'])
# def login(usuario:schemas.users.UserLogin):
#     if usuario.usuario == 'rlunas' and usuario.password == '1234':
#         token:str=solicita_token(usuario.dict())
#         return JSONResponse(status_code=200, content=token)
#     else:
#         return JSONResponse(content={'mensaje':'Acceso denegado'},status_code=404)