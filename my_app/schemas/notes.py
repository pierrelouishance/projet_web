
from datetime import datetime

from pydantic import BaseModel, Field




class NoteSchema(BaseModel):
    id: str
    titre: str 
    auteur_ : str 
    texte: str 
    categorie: str 
