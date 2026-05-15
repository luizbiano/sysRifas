from sqlalchemy import Column, String, Date, DateTime, ForeignKey
from app.core.database import Base
from app.model.base_model import AuditModel


class UsuarioModel(Base, AuditModel):

    __tablename__ = "usuario"

    id = Column(String(3), primary_key=True)
    nome = Column(String(100), nullable=False)
    dt_nascimento = Column(Date, nullable=False)

    email = Column(String(100), nullable=False, unique=True)

    telefone = Column(String(20), nullable=False)

    senha = Column(String(256), nullable=False)

    alterar_senha = Column(String(1), nullable=False)

    id_perfil = Column(
        String(3),
        ForeignKey("perfil.id"),
        nullable=False
    )