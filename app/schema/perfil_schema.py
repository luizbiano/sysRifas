from pydantic import BaseModel
from datetime import datetime

class PerfilBase(BaseModel):

    descricao: str

class PerfilCreate(PerfilBase):

    pass

class PerfilResponse(PerfilBase):
    id: str

    dt_inclusao: datetime
    usr_inclusao: str

    dt_modificacao: datetime
    usr_modificacao: str

class PerfilUpdateSchema(BaseModel):

    descricao: str | None = None