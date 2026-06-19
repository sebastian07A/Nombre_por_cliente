from fastapi import FastAPI
from datetime import datetime

app = FastAPI()


@app.get("/")
def inicio():
    return{"mensaje": "hola aprendices 3407180"}

@app.get("/saludar")
def saludar():
    return {"saludo": "hola soy..."}

@app.get("/hora")
def hora ():
    return {"hora": datetime()}  
       
@app.get("saludar/{nombre}/{apellido}/{Edad}")
def saludar2(nombre, apellido, Edad):
    return {"saludo": f"Hola soy{nombre} {apellido} {Edad}"}

@app.get("/amigos")
def lista_amigos():
    amigos = [
        "Sebas",
        "Cami",
        "Matias",
        "Tban",
        "Samuel"
    ]
    return {"amigos": amigos}

@app.get("/amigos/{id}")
def obtener_amigos(id: int):
         return {"amigos": amigos[id]}