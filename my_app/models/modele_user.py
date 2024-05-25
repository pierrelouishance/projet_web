from sqlalchemy import String, ForeignKey, Float
from sqlalchemy.orm import relationship, mapped_column, Mapped
from typing import Optional 
from my_app.database import Base


class User(Base):
    __tablename__ = "user"

    id      = mapped_column(String(50), primary_key=True)
    name    = mapped_column(String(50), nullable=False, unique=True)
    mdp   = mapped_column(String(50), nullable=False)

