from sqlalchemy import Column, ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import Mapped

from database.models.base import Base


class PatternRequirementsDb(Base):
    __tablename__ = "pattern_requirements"

    pattern: Mapped[int] = Column(
        "pattern",
        Integer,
        ForeignKey(
            "patterns.id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        primary_key=True,
        nullable=False,
    )
    thread: Mapped[int] = Column(
        "thread",
        Integer,
        ForeignKey("threads.id", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
    )

    __table_args__ = (UniqueConstraint("pattern", "thread", name="pattern_thread_uix"),)
