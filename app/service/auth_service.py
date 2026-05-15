from fastapi import HTTPException
from app.core.constants import MessageConstants,SeedConstants
from app.data.usuario_data import UsuarioData
from app.schema.auth_schema import UsuarioLogado

class AuthService:

    @staticmethod
    def get_usuario_logado(db, email: str) -> UsuarioLogado:

        usuario = UsuarioData.get_by_email(db, email)

        if not usuario:

            raise HTTPException(
                status_code=403,
                detail=MessageConstants.SEM_PERMISSAO
            )

        return UsuarioLogado(
            id=usuario.id,
            email=usuario.email,
            id_perfil=usuario.id_perfil
        )

    @staticmethod
    def validar_admin(usuario_logado: UsuarioLogado):

        if usuario_logado.id_perfil != SeedConstants.ADMIN.PERFIL_ID:

            raise HTTPException(
                status_code=403,
                detail=MessageConstants.SEM_PERMISSAO
            )