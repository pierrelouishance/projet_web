from sqlalchemy import String, ForeignKey, Float
from sqlalchemy.orm import relationship, mapped_column, Mapped
from typing import Optional 
from my_app.database import Base

class Note(Base):
    __tablename__ = "notes"

    id  = mapped_column(String, primary_key=True)
    titre = mapped_column(String(50), nullable=False)
    auteur_id: Mapped[str] = mapped_column(ForeignKey("user.id"))
    texte = mapped_column(String(1000), nullable=False)
    categorie = mapped_column(String(50), nullable=False)

