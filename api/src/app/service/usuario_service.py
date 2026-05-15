import email

from fastapi import HTTPException
from app.core.constants import MessageConstants, FieldConstants
from app.data.perfil_data import PerfilData
from app.data.usuario_data import UsuarioData
from app.model.usuario_model import UsuarioModel
from datetime import datetime

from app.service.auth_service import AuthService
class UsuarioService:

    @staticmethod
    def get_all(db, email):

        if not email:
            raise Exception(MessageConstants.CAMPO_OBRIGATORIO +" - "+ FieldConstants.EMAIL)

        #AuthService.validar_admin(db, email)
        usuario_logado = AuthService.get_usuario_logado(db, email)
        AuthService.validar_admin(usuario_logado)

        return UsuarioData.get_all(db)
    
    @staticmethod
    def create(db, email: str, usuario_data):

        if not email:
            raise Exception(MessageConstants.CAMPO_OBRIGATORIO +" - "+ FieldConstants.EMAIL)

        #AuthService.validar_admin(db, email)    
        usuario_logado = AuthService.get_usuario_logado(db, email)
        AuthService.validar_admin(usuario_logado)

        novo_id = UsuarioData.get_next_id(db)

        novo_usuario = UsuarioModel(
            #id=usuario_data.id,
            id=novo_id,
            nome=usuario_data.nome,
            dt_nascimento=usuario_data.dt_nascimento,
            email=usuario_data.email,
            telefone=usuario_data.telefone,
            senha=usuario_data.senha,
            alterar_senha=usuario_data.alterar_senha,
            id_perfil=usuario_data.id_perfil,

            dt_inclusao=datetime.now(),
            dt_modificacao=datetime.now(),

            usr_inclusao=usuario_logado.id,
            usr_modificacao=usuario_logado.id
        )

        return UsuarioData.create(db, novo_usuario)
    
    @staticmethod
    def delete(db, id: str, email: str):

        #AuthService.validar_admin(db, email)
        usuario_logado = AuthService.get_usuario_logado(db, email)
        AuthService.validar_admin(usuario_logado)

        usuario = UsuarioData.get_by_id(db, id)

        if not usuario:

            raise HTTPException(
                status_code=404,
                detail=MessageConstants.NAO_ENCONTRADO +" - "+ FieldConstants.USUARIO
            )

        if id == "001":
            raise HTTPException(
                status_code=400,
                detail=MessageConstants.NAO_EXCLUIR +" - "+ FieldConstants.USUARIO
            )

        return UsuarioData.soft_delete(
            db,
            usuario,
            usuario_logado.id
        )
    
    @staticmethod
    def get_by_id(db, id: str, email: str):

        #AuthService.validar_admin(db, email)
        usuario_logado = AuthService.get_usuario_logado(db, email)
        AuthService.validar_admin(usuario_logado)

        usuario = UsuarioData.get_by_id(db, id)

        if not usuario:

            raise HTTPException(
                status_code=404,
                detail=MessageConstants.NAO_ENCONTRADO +" - "+ FieldConstants.USUARIO
            )

        return usuario
    
    @staticmethod
    def update(db, id: str, usuario_data, email: str):

        #AuthService.validar_admin(db, email)
        usuario_logado = AuthService.get_usuario_logado(db, email)
        AuthService.validar_admin(usuario_logado)

        if id == "001":

            raise HTTPException(
                status_code=403,
                detail=MessageConstants.NAO_ALTERAR +" - "+ FieldConstants.USUARIO
            )

        usuario = UsuarioData.update(
            db,
            id,
            usuario_data,
            usuario_logado.id
        )

        if not usuario:

            raise HTTPException(
                status_code=404,
                detail=MessageConstants.NAO_ENCONTRADO +" - "+ FieldConstants.USUARIO
            )

        return usuario