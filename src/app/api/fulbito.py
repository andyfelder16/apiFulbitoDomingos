from fastapi import APIRouter
from sqlalchemy.orm import sessionmaker

from api.models import CourseCreate, CourseUpdate, CourseFilter, Hashtags, ReviewCreate, ContentCreate
from db import Player, Match

router = APIRouter()

session = None
engine = None


def set_engine(engine_rcvd):
    global engine
    global session
    engine = engine_rcvd
    session = sessionmaker(bind=engine)()
    return session


@router.get('/true')
async def get_true():
    return True
