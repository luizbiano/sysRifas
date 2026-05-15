from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from app.schema.perfil_schema import PerfilCreate
from app.service.perfil_service import PerfilService
from app.schema.perfil_schema import PerfilUpdateSchema 
from app.core.database import SessionLocal
from typing import List
from app.schema.perfil_schema import PerfilResponse

router = APIRouter(
    prefix="/perfil",
    tags=["Perfil"]
)

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

@router.get("/",response_model=List[PerfilResponse])
def get_all(email: str, db: Session = Depends(get_db)):
    return PerfilService.get_all(db,email)

@router.post("/perfil")
def create_perfil(
    email: str,
    perfil: PerfilCreate,
    db: Session = Depends(get_db)
):

    return PerfilService.create(db, email, perfil)

@router.delete("/{id}")
def delete_perfil(
    id: str,
    email: str,
    db: Session = Depends(get_db)
):

    return PerfilService.delete(
        db,
        id,
        email
    )

@router.get("/{id}",response_model=PerfilResponse)
def get_by_id(
    id: str,
    email: str,
    db: Session = Depends(get_db)
):

    return PerfilService.get_by_id(
        db,
        id,
        email
    )

@router.put("/{id}")
def update_perfil(
    id: str,
    perfil_data: PerfilUpdateSchema,
    email: str,
    db: Session = Depends(get_db)
):

    return PerfilService.update(
        db,
        id,
        perfil_data,
        email
    )