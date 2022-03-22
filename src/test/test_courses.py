import asyncio
import uuid
from fastapi import status
from app.api import fulbito
from app.api.models import CourseCreate, CourseUpdate, CourseFilter, Hashtags, ReviewCreate


def test_true():
    assert True is True
