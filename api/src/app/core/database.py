from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

import time

DATABASE_URL = ("postgresql://postgres:postgres@db:5432/sysrifas")

MAX_RETRIES = 10
RETRY_INTERVAL = 3

engine = None

for attempt in range(MAX_RETRIES):

    try:

        engine = create_engine(DATABASE_URL)

        connection = engine.connect()

        connection.close()

        print("Banco conectado com sucesso!")

        break

    except Exception as ex:

        print(
            f"Tentativa {attempt + 1} falhou: {ex}"
        )

        time.sleep(RETRY_INTERVAL)

if engine is None:

    raise Exception(
        "Não foi possível conectar ao banco."
    )

#engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()