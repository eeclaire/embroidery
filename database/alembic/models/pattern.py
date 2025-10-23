from __future__ import annotations

from typing import Any

from sqlalchemy import Column, Integer, UniqueConstraint, VARCHAR
from sqlalchemy.orm import Mapped

from .base import Base


class PatternDb(Base):
    __tablename__ = "patterns"

    id: Mapped[int] = Column("id", Integer, primary_key=True, autoincrement=True)
    source_id: Mapped[str] = Column("source_id", VARCHAR)

    __table_args__ = (UniqueConstraint("facility_code", "name"),)

    UPSERT_INDEX_COLUMNS = ["facility_code", "name"]

    def __repr__(self) -> str:
        return (
            f"<MeasurementSeries(id={self.id}, facility_code={self.facility_code}, "
            f"name={self.name}>"
        )

    def to_dict(self) -> dict[str, Any]:
        result = {
            "facility_code": self.facility_code,
            "name": self.name,
            "uom": self.uom,
            "datatype": self.datatype,
        }
        if self.id is not None:
            result["id"] = self.id

        return result
