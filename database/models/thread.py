from __future__ import annotations

from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.orm import Mapped

from database.models.base import Base


class ThreadDb(Base):
    __tablename__ = "threads"

    id: Mapped[int] = Column("id", Integer, primary_key=True, autoincrement=True)
    color_code: Mapped[str] = Column(
        "color_code",
        VARCHAR(length=8),
        unique=True,
        nullable=False,
    )  # DMC inventory color code

    # human-recognizable color
    color_desc: Mapped[str] = Column("color_desc", VARCHAR(length=32), nullable=True)
