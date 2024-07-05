from fastapi import FastAPI
from routes.persona import persona
from routes.usuarios import usuario
from routes.users import user


app = FastAPI()
app.include_router(persona)
app.include_router(usuario)
app.include_router(user)

print ("Bienvenido a mi aplicación")