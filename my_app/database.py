from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, DeclarativeBase, sessionmaker

engine = create_engine("sqlite:///data/db.sqlite", echo=True)
Session =sessionmaker(engine)


class Base(DeclarativeBase): 
    pass

from my_app.models.modele_note import Note
from my_app.models.modele_user import User
from my_app.models.modele_partage import Partage


def create_database() :
    Base.metadata.create_all(engine)

def delete_database():
    Base.metadata.clear()