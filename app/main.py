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
         return {"amigos": amigo[id]}

#usuarios
lista_clientes = [
    {"id": 1, "nombre":"Sebastian", "email": "sebastian@gmail.com", "edad": 18, "descripción":"N"},
    {"id": 2, "nombre":"Cami", "email": "cami@gmail.com", "edad": 17, "descripción":"NA"},
    {"id": 3, "nombre":"Esteban", "email": "Esteban@gmail.com", "edad": 20, "descripción":"NA"},
    {"id": 4, "nombre":"Maria", "email": "Maria@gmail.com", "edad": 10, "descripción":"NA"},
    {"id": 5, "nombre":"Enrique", "email": "Enrique@gmail.com", "edad": 38, "descripción":"NA"}
]
@app.get("/clientes")
def listar_clientes():
    return lista_clientes