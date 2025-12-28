from sqlalchemy import Column, ForeignKey, Integer

from database.models.base import Base


class InventoryDb(Base):
    __tablename__ = "inventory"

    color: int = Column(
        "thread",
        Integer,
        ForeignKey("threads.id", onupdate="CASCADE"),
        primary_key=True,
        nullable=False,
    )

    qty: int = Column("qty", Integer, nullable=False)
