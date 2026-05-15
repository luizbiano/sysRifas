from fastapi import HTTPException

from app.data.perfil_data import PerfilData
from app.model.perfil_model import PerfilModel
from datetime import datetime
from app.service.auth_service import AuthService
from app.core.constants import MessageConstants, EntityConstants, FieldConstants

class PerfilService:

    @staticmethod
    def get_all(db, email: str):

        if not email:
            raise Exception(MessageConstants.CAMPO_OBRIGATORIO +" - "+ FieldConstants.EMAIL)

        usuario_logado = AuthService.get_usuario_logado(db, email)
        AuthService.validar_admin(usuario_logado)
        #AuthService.validar_admin(db, email)

        return PerfilData.get_all(db)

    @staticmethod
    def create(db, email: str, perfil_data):

        if not email:
            raise Exception(MessageConstants.CAMPO_OBRIGATORIO +" - "+ FieldConstants.EMAIL)

        #AuthService.validar_admin(db, email)
        usuario_logado = AuthService.get_usuario_logado(db, email)
        AuthService.validar_admin(usuario_logado)

        novo_id = PerfilData.get_next_id(db)

        novo_perfil = PerfilModel(

            id=novo_id,
            descricao=perfil_data.descricao,
            dt_inclusao=datetime.now(),
            dt_modificacao=datetime.now(),
            usr_inclusao=usuario_logado.id,
            usr_modificacao=usuario_logado.id
        )

        return PerfilData.create(db, novo_perfil)
    
    @staticmethod
    def delete(db, id: str, email: str):

        #AuthService.validar_admin(db, email)
        usuario_logado = AuthService.get_usuario_logado(db, email)
        AuthService.validar_admin(usuario_logado)

        perfil = PerfilData.get_by_id(db, id)

        if not perfil:

            raise HTTPException(
                status_code=404,
                detail=MessageConstants.NAO_ENCONTRADO +" - "+ FieldConstants.PERFIL
            )

        if id == "001":
            raise HTTPException(
                status_code=400,
                detail=MessageConstants.NAO_EXCLUIR +" - "+ FieldConstants.PERFIL
            )

        return PerfilData.soft_delete(
            db,
            perfil,
            usuario_logado.id
        )

    @staticmethod
    def get_by_id(db, id: str, email: str):

        #AuthService.validar_admin(db, email)
        usuario_logado = AuthService.get_usuario_logado(db, email)
        AuthService.validar_admin(usuario_logado)

        perfil = PerfilData.get_by_id(db, id)

        if not perfil:
            raise HTTPException(
                status_code=404,
                detail=MessageConstants.NAO_ENCONTRADO +" - "+ FieldConstants.PERFIL
            )

        return perfil

    @staticmethod
    def update(db, id: str, perfil_data, email: str):

        #AuthService.validar_admin(db, email)
        usuario_logado = AuthService.get_usuario_logado(db, email)
        AuthService.validar_admin(usuario_logado)

        if id == "001":

            raise HTTPException(
                status_code=403,
                detail=MessageConstants.NAO_ALTERAR +" - "+ FieldConstants.PERFIL
            )

        perfil = PerfilData.update(
            db,
            id,
            perfil_data,
            usuario_logado.id
        )

        if not perfil:

            raise HTTPException(
                status_code=404,
                detail=MessageConstants.NAO_ENCONTRADO +" - "+ FieldConstants.PERFIL
            )

        return perfil    