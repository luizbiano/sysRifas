from sqlalchemy import Column, String, DateTime
from app.core.database import Base
from app.model.base_model import AuditModel

class PerfilModel(Base, AuditModel):

    __tablename__ = "perfil"

    id = Column(String(3), primary_key=True)

    descricao = Column(String(50), nullable=False)
