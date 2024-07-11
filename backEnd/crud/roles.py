import models.roles
import schemas.roles
from sqlalchemy.orm import Session
#import models, schemas

def get_rol(db: Session, id: int):
    return db.query(models.roles.Rol).filter(models.roles.Rol.id == id).first()

def get_rol_by_usuario(db: Session, usuario: str):
    return db.query(models.roles.User).filter(models.roles.Rol.roles == roles).first()

def get_roles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.roles.Rol).offset(skip).limit(limit).all()

def create_rol(db: Session, user: schemas.roles.RolCreate):
    db_rol = models.roles.Rol(rol=user.usuario, password=user.password, created_at=user.created_at, estatus=user.estatus, Id_persona=user.Id_persona)
    db.add(db_rol)
    db.commit()
    db.refresh(db_rol)
    return db_rol

def update_user(db: Session, id: int, user: schemas.users.UserUpdate):
    db_user = db.query(models.users.User).filter(models.users.User.id == id).first()
    if db_user:
        for var, value in vars(user).items():
            setattr(db_user, var, value) if value else None
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, id: int):
    db_user = db.query(models.users.User).filter(models.users.User.id == id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user