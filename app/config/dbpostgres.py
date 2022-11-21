from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from dotenv import load_dotenv
import databases 
import os

db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")
db_host = os.environ.get("DB_HOST")
db_port = os.environ.get("DB_PORT")

DATABASE_URL = "postgresql://postgres:admin@localhost:5432/erp"
# database = databases.Database(DATABASE_URL)

engine = create_engine(DATABASE_URL, echo=True)

# SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
default_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))


Base = declarative_base()


def get_db():
    db = default_session()
    try:
        yield db
    finally:
        db.close