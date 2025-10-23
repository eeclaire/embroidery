from typing import List, Optional

from pydantic import BaseModel, Field


class Color(BaseModel):
    code: str
    brand: str
    description: str | None


class ValidationResult(BaseModel):
    is_valid: bool = Field(description="Whether the DataFrame passed validation")
    errors: List[str] = Field(
        default_factory=list, description="Validation errors that prevent data usage"
    )
    warnings: List[str] = Field(
        default_factory=list, description="Validation warnings for data quality issues"
    )


class EmbroideryPattern(BaseModel):
    pattern_name: str = Field(description="Name or title of the embroidery pattern")
    designer: Optional[str] = Field(None, description="Designer or brand name")
    difficulty_level: Optional[str] = Field(
        None, description="Beginner, Intermediate, Advanced, etc."
    )
    colors: List[Color] = Field(
        default_factory=list, description="Colors and thread information"
    )
