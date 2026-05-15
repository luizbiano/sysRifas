from datetime import datetime

from sqlalchemy.orm import Session

from app.model.perfil_model import PerfilModel
from app.model.usuario_model import UsuarioModel
from app.core.constants import SeedConstants

def create_initial_data(db: Session):

    perfil_admin = db.query(PerfilModel).filter(
        PerfilModel.id == "001"
    ).first()

    if not perfil_admin:

        perfil = PerfilModel(
            id=SeedConstants.ADMIN.PERFIL_ID,
            descricao=SeedConstants.ADMIN.PERFIL_DESCRICAO,
            dt_inclusao=datetime.now(),
            dt_modificacao=datetime.now(),
            usr_inclusao=SeedConstants.SYSTEM.USER,
            usr_modificacao=SeedConstants.SYSTEM.USER
        )

        db.add(perfil)

        usuario = UsuarioModel(
            id=SeedConstants.ADMIN.USUARIO_ID,
            nome=SeedConstants.ADMIN.NOME,
            dt_nascimento=datetime.strptime(SeedConstants.ADMIN.DATA_NASCIMENTO, "%Y-%m-%d"),
            email=SeedConstants.ADMIN.EMAIL,
            telefone=SeedConstants.ADMIN.TELEFONE,
            senha=SeedConstants.ADMIN.SENHA,
            alterar_senha=SeedConstants.ADMIN.ALTERAR_SENHA,
            id_perfil=SeedConstants.ADMIN.PERFIL_ID,
            dt_inclusao=datetime.now(),
            dt_modificacao=datetime.now(),
            usr_inclusao=SeedConstants.SYSTEM.USER,
            usr_modificacao=SeedConstants.SYSTEM.USER
        )

        db.add(usuario)

        db.commit()

        print("Dados iniciais criados com sucesso!")

    else:

        print("Dados iniciais já existem.")