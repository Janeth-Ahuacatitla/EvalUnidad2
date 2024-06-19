from fastapi import APIRouter

persona = APIRouter()

@persona.get("/personas")

def helloworld():
    return "Hello World"