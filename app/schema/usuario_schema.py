from pyclbr import Class
from typing import Optional

from pydantic import BaseModel
from datetime import date, datetime

class UsuarioBase(BaseModel):

    nome: str
    dt_nascimento: date
    email: str
    telefone: str
    senha: str
    alterar_senha: str
    id_perfil: str

class UsuarioCreate(UsuarioBase):

    pass

class UsuarioResponse(UsuarioBase):

    id: str
    dt_inclusao: datetime
    usr_inclusao: str

    dt_modificacao: datetime
    usr_modificacao: str


class UsuarioUpdateSchema(BaseModel):

    nome: Optional[str] = None
    dt_nascimento: Optional[date] = None
    email: Optional[str] = None
    telefone: Optional[str] = None
    senha: Optional[str] = None
    alterar_senha: Optional[str] = None
    id_perfil: Optional[str] = None