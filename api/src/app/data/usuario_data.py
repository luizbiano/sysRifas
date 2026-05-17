from fastapi import HTTPException
from sqlalchemy import func
from sqlalchemy.exc import IntegrityError 
from app.model.usuario_model import UsuarioModel
from datetime import datetime
from app.data.base_data import BaseData
from app.core.constants import DeleteConstants, MessageConstants

class UsuarioData(BaseData):

    model = UsuarioModel

    @staticmethod
    def get_by_email(db, email: str):

        return (
            db.query(UsuarioModel)
            .filter(
                UsuarioModel.email == email,
                UsuarioModel.fl_delete == DeleteConstants.ATIVO
            )
            .first()
        )

    @staticmethod
    def create(db, usuario):

        try:

            db.add(usuario)
            db.commit()
            db.refresh(usuario)

            return usuario

        except IntegrityError as ex:

            db.rollback()

            # verifica se foi erro de email duplicado
            if "usuario_email_key" in str(ex):

                usuario_deletado = (
                    db.query(UsuarioModel)
                    .filter(
                        UsuarioModel.email == usuario.email,
                        UsuarioModel.fl_delete == DeleteConstants.DELETADO
                    )
                    .first()
                )

                if usuario_deletado:

                    usuario_deletado.nome = usuario.nome
                    usuario_deletado.dt_nascimento = usuario.dt_nascimento
                    usuario_deletado.telefone = usuario.telefone
                    usuario_deletado.senha = usuario.senha
                    usuario_deletado.alterar_senha = usuario.alterar_senha
                    usuario_deletado.id_perfil = usuario.id_perfil

                    # RESTAURA SOFT DELETE
                    usuario_deletado.fl_delete = DeleteConstants.ATIVO
                    usuario_deletado.dt_delete = None
                    usuario_deletado.usr_delete = None

                    # auditoria
                    usuario_deletado.dt_modificacao = datetime.now()
                    usuario_deletado.usr_modificacao = "System"

                    db.commit()
                    db.refresh(usuario_deletado)

                    return usuario_deletado

            raise ex
    
    @staticmethod
    def update(db, id, usuario_data, email):

        usuario = db.query(UsuarioModel).filter(
            UsuarioModel.id == id,
            UsuarioModel.fl_delete == DeleteConstants.ATIVO
        ).first()

        if not usuario:
            return None

        dados_update = usuario_data.dict(exclude_unset=True)

        houve_alteracao = UsuarioData.update_fields(
            usuario,
            dados_update
        )

        if not houve_alteracao:

            raise HTTPException(
                status_code=400,
                detail=MessageConstants.NENHUMA_ALTERACAO
            )

        usuario.dt_modificacao = datetime.now()
        usuario.usr_modificacao = email

        db.commit()
        db.refresh(usuario)

        return usuario
    
    @staticmethod
    def login(db, email: str, senha: str):

        return (
            db.query(UsuarioModel)
            .filter(
                UsuarioModel.email == email,
                UsuarioModel.senha == senha,
                UsuarioModel.fl_delete == "F"
            )
            .first()
        )