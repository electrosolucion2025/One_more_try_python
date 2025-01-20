from fastapi import FastAPI
from app.routes import openai_routes

app = FastAPI(title="My API")

# Incluir rutas
app.include_router(openai_routes.router)

@app.get("/")
def read_root():
    return {"message": "Bienvenido a mi backend en FastAPI"}