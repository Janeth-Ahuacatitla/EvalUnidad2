from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from cryptography.fernet import Fernet
import crud.roles, config.db, schemas.roles, models.roles
from typing import List

key=Fernet.generate_key()
f = Fernet(key)

roles = APIRouter()

models.roles.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@roles.get("/roles/", response_model=List[schemas.roles.roles], tags=["roles"])
def read_roles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    db_roles= crud.roles.get_roles(db=db, skip=skip, limit=limit)
    return db_roles

@roles.post("/roles/{id}", response_model=schemas.roles.roles, tags=["roles"])
def read_user(id: int, db: Session = Depends(get_db)):
    db_roles= crud.roles.get_roles(db=db, id=id)
    if db_roles is None:
        raise HTTPException(status_code=404, detail="roles no encontrada")
    return db_roles

@roles.post("/roles/", response_model=schemas.roles.roles, tags=["roles"])
def create_roles(roles: schemas.roles.rolesCreate, db: Session = Depends(get_db)):
    db_roles = crud.roles.get_roles_by_nombre(db, roles=roles.Nombre)
    if db_roles:
        raise HTTPException(status_code=400, detail="Usuario existente intenta nuevamente")
    return crud.roles.create_roles(db=db, roles=roles)

@roles.put("/roles/{id}", response_model=schemas.roles.roles, tags=["roles"])
def update_roles(id: int, roles: schemas.roles.rolesUpdate, db: Session = Depends(get_db)):
    db_roles = crud.roles.update_roles(db=db, id=id, roles=roles)
    if db_roles is None:
        raise HTTPException(status_code=404, detail="roles no existe, no actualizado")
    return db_roles

@roles.delete("/roles/{id}", response_model=schemas.roles.roles, tags=["roles"])
def delete_roles(id: int, db: Session = Depends(get_db)):
    db_roles = crud.roles.delete_roles(db=db, id=id)
    if db_roles is None:
        raise HTTPException(status_code=404, detail="roles no existe, no se pudo eliminar")
    return db_roles