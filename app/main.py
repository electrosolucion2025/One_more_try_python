from fastapi import FastAPI

from app.routes import openai_routes, payment_routes, printer_routes

app = FastAPI(title="My API")

# Incluir rutas
app.include_router(openai_routes.router)
app.include_router(payment_routes.router)
app.include_router(printer_routes.router)

@app.get("/")
def read_root():
    return {"message": "Proyecto realizado por ElectroSolucion y ***"}