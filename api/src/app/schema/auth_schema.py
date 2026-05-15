from pydantic import BaseModel

class UsuarioLogado(BaseModel):

    id: str
    email: str
    id_perfil: str