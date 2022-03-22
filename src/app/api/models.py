from pydantic import BaseModel, Field
from uuid import UUID
from typing import List, Optional
from fastapi import Query


class CourseBase(BaseModel):
    sub_level: Optional[int] = Field(None, ge=0, le=2)
    latitude: Optional[float] = Field(None, ge=-180, le=180)
    longitude: Optional[float] = Field(None, ge=-90, le=90)
    category: Optional[str]
