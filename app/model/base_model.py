from sqlalchemy import Column, DateTime, String, Boolean
from app.core.constants import DeleteConstants
from datetime import datetime


class AuditModel:

    dt_inclusao = Column(
        DateTime,
        nullable=False,
        default=datetime.now
    )

    dt_modificacao = Column(
        DateTime,
        nullable=False,
        default=datetime.now,
        onupdate=datetime.now
    )

    usr_inclusao = Column(
        String,
        nullable=False
    )

    usr_modificacao = Column(
        String,
        nullable=False
    )

    fl_delete = Column(
    String,
    nullable=False,
    default=DeleteConstants.ATIVO
    )

    dt_delete = Column(
        DateTime,
        nullable=True
    )

    usr_delete = Column(
        String,
        nullable=True
    )