from fastapi import HTTPException
from datetime import datetime
from app.core.constants import DeleteConstants

class BaseData:

    model = None

    @classmethod
    def get_all(cls, db):

        return db.query(cls.model).filter(
            cls.model.fl_delete == DeleteConstants.ATIVO
        ).all()

    @classmethod
    def get_by_id(cls, db, id):

        return db.query(cls.model).filter(
            cls.model.id == id,
            cls.model.fl_delete == DeleteConstants.ATIVO
        ).first()

    @classmethod
    def get_next_id(cls, db):

        ultimo = db.query(cls.model).order_by(
            cls.model.id.desc()
        ).first()

        if not ultimo:
            return "001"

        novo_id = int(ultimo.id) + 1

        return str(novo_id).zfill(3)

    @classmethod
    def create(cls, db, obj):

        db.add(obj)

        try:

            db.commit()
            db.refresh(obj)

            return obj

        except Exception as ex:

            db.rollback()
            raise ex

    @classmethod
    def soft_delete(cls, db, obj, email):

        obj.fl_delete = DeleteConstants.DELETADO
        obj.dt_delete = datetime.now()
        obj.usr_delete = email

        obj.dt_modificacao = datetime.now()
        obj.usr_modificacao = email

        db.commit()
        db.refresh(obj)

        return obj

    @classmethod
    def update(cls, db, id, dados_update, email):

        obj = cls.get_by_id(db, id)

        if not obj:
            return None

        houve_alteracao = False

        dados = dados_update.dict(exclude_unset=True)

        for campo, valor in dados.items():

            valor_atual = getattr(obj, campo)

            if valor in [None, ""]:
                continue

            if valor == valor_atual:
                continue

            setattr(obj, campo, valor)

            houve_alteracao = True

        if not houve_alteracao:

            raise HTTPException(
                status_code=400,
                detail="Nenhuma alteração realizada"
            )

        obj.dt_modificacao = datetime.now()
        obj.usr_modificacao = email

        db.commit()
        db.refresh(obj)

        return obj
    
    @staticmethod
    def update_fields(obj, dados_update):

        houve_alteracao = False

        for campo, valor in dados_update.items():

            valor_atual = getattr(obj, campo)

            # ignora vazio
            if valor in [None, ""]:
                continue

            # ignora valores iguais
            if valor == valor_atual:
                continue

            setattr(obj, campo, valor)

            houve_alteracao = True

        return houve_alteracao