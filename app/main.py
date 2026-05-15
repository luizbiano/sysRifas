from fastapi import FastAPI
from app.controller.perfil_controller import router as perfil_router
from app.controller.usuario_controller import router as usuario_router
from app.core.database import Base, engine, SessionLocal

# IMPORTAR TODOS OS MODELS
from app.model.perfil_model import PerfilModel
from app.model.usuario_model import UsuarioModel
from app.seed.initial_data import create_initial_data

app = FastAPI()
app.include_router(perfil_router)
app.include_router(usuario_router)
Base.metadata.create_all(bind=engine)
db = SessionLocal()

create_initial_data(db)

db.close()

@app.get("/")
def home():
    return {"message": "API SysRifas online"}