from pydantic import BaseModel
from datetime import datetime


class AuditSchema(BaseModel):

    dt_inclusao: datetime | None = None
    dt_modificacao: datetime | None = None

    usr_inclusao: str | None = None
    usr_modificacao: str | None = None

    fl_delete: str | None = None
    dt_delete: datetime | None = None
    usr_delete: str | None = None    