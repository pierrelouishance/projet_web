from sqlalchemy import String, ForeignKey, Float,PrimaryKeyConstraint
from sqlalchemy.orm import relationship, mapped_column, Mapped
from typing import Optional 
from my_app.database import Base



class Partage(Base):
    __tablename__ = "partage"

    user_id: Mapped[str] = mapped_column(ForeignKey("user.id"),primary_key=True)
    note_id: Mapped[str] = mapped_column(ForeignKey("user.id"),primary_key=True)

    __table_args__ = (
        PrimaryKeyConstraint('user_id', 'note_id', name='my_table_pk'),
    )



