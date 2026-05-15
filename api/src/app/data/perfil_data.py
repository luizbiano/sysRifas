from sqlalchemy import func
from sqlalchemy.orm import Session
from app.model.perfil_model import PerfilModel
from app.model.usuario_model import UsuarioModel
from datetime import datetime
from app.data.base_data import BaseData
from app.core.constants import DeleteConstants

class PerfilData(BaseData):

    model = PerfilModel
    
    @staticmethod
    def update(db, id: str, perfil_data, email: str):

        perfil = db.query(PerfilModel).filter(
            PerfilModel.id == id,
            PerfilModel.fl_delete == DeleteConstants.ATIVO
        ).first()

        if not perfil:
            return None

        perfil.descricao = perfil_data.descricao

        perfil.dt_modificacao = datetime.now()
        perfil.usr_modificacao = email

        db.commit()
        db.refresh(perfil)

        return perfil