from __future__ import annotations

from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import Mapped
from sqlalchemy.schema import Index

from database.models.base import Base


class PatternDb(Base):
    __tablename__ = "patterns"

    id: Mapped[int] = Column("id", Integer, primary_key=True, autoincrement=True)
    source_id: Mapped[str] = Column("source_id", VARCHAR, unique=True, nullable=False)

    name: Mapped[str] = Column("name", VARCHAR)

    __table_args__ = (Index("idx_name", "name"),)
