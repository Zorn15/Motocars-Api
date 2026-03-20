import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.database import engine, Base
from app.routers import brands, cars

# Crear tablas
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="MotorsCars API",
    description="API REST para el mercado de autos MotorsCars",
    version="1.0.0",
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(brands.router)
app.include_router(cars.router)

# Servir el frontend desde FastAPI
FRONTEND_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "..", "frontend")
FRONTEND_DIR = os.path.abspath(FRONTEND_DIR)

if os.path.isdir(FRONTEND_DIR):
    @app.get("/")
    def serve_index():
        return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))

    @app.get("/{filename}.html")
    def serve_html(filename: str):
        filepath = os.path.join(FRONTEND_DIR, f"{filename}.html")
        if os.path.isfile(filepath):
            return FileResponse(filepath)
        return {"error": "No encontrado"}

    app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")
else:
    @app.get("/")
    def root():
        return {"message": "MotorsCars API v1.0", "docs": "/docs"}
