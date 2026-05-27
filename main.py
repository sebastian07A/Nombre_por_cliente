from fastapi import FastAPI

app = FastAPI()

# Endpoint principal
@app.get("/")
def inicio():
    return {
        "mensaje": "Este es el proyecto de clientes a desarrollar"
    }

# Endpoint de clientes
@app.get("/clientes")
def obtener_clientes():
    clientes = [
        "Juan",
        "María",
        "Carlos",
        "Ana",
        "Pedro"
    ]

    return {
        "clientes": clientes
    }