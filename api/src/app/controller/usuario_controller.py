from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schema.usuario_schema import UsuarioCreate
from app.schema.usuario_schema import UsuarioUpdateSchema
from app.service.usuario_service import UsuarioService
from typing import List
from app.schema.usuario_schema import UsuarioResponse
from app.schema.auth_schema import LoginSchema

router = APIRouter(
    prefix="/usuario",
    tags=["Usuario"]
)

@router.get("/", response_model=List[UsuarioResponse])
def get_all(
    email: str,
    db: Session = Depends(get_db)
):

    return UsuarioService.get_all(db, email)

@router.post("/usuario")
def create_usuario(
    email: str,
    usuario: UsuarioCreate,
    db: Session = Depends(get_db)
):

    return UsuarioService.create(db, email, usuario)

@router.delete("/{id}")
def delete_usuario(
    id: str,
    email: str,
    db: Session = Depends(get_db)
):

    return UsuarioService.delete(
        db,
        id,
        email
    )

@router.get("/{id}",response_model=UsuarioResponse)
def get_by_id(
    id: str,
    email: str,
    db: Session = Depends(get_db)
):

    return UsuarioService.get_by_id(
        db,
        id,
        email
    )

@router.put("/{id}")
def update_usuario(
    id: str,
    usuario_data: UsuarioUpdateSchema,
    email: str,
    db: Session = Depends(get_db)
):

    return UsuarioService.update(
        db,
        id,
        usuario_data,
        email
    )

@router.post("/login")
def login(
    login_data: LoginSchema,
    db: Session = Depends(get_db)
):

    return UsuarioService.login(
        db,
        login_data
    )