from datetime import datetime

from uuid import uuid4
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from my_app.schemas.notes import NoteSchema
from my_app.database import Session
from my_app.models.modele_note import Note


def get_db():
    return Session()
# by PL
def get_all_notes():
    with get_db() as db:
        return db.query(Note).all()
    

def add_note(db: Session, titre: str, categorie: str, texte: str, auteur_id: str):
    note = Note(id=str(uuid.uuid4()), titre=titre, categorie=categorie, texte=texte, auteur_id=auteur_id)
    db.add(note)
    db.commit()
    db.refresh(note)
    return note