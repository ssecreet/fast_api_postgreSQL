from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

from config import POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, SQLALCHEMY_DATABASE_URI


url = URL.create(
    drivername="postgresql",
    username=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
    host=POSTGRES_HOST,
    port=5432,
    database=POSTGRES_DB
)

# engine = create_engine(url)  # движок для подключения к БД
engine = create_engine(SQLALCHEMY_DATABASE_URI)

Session = sessionmaker(bind=engine)


def db_session():
    db = Session()
    try:
        yield db
    finally:
        db.close()
