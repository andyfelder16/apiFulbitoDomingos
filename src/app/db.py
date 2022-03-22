from sqlalchemy import (
    Column,
    Table,
    ForeignKey,
    create_engine
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, relationship
from sqlalchemy.sql import func
from sqlalchemy.sql.sqltypes import Date, String, Integer


DATABASE_URL = "postgresql://jhveahofefzvsq:eb0250343f5b7772d0db89b4c6ac263c7d1c891b956d4f38527acfc2ba0e88b6@ec2-3-221-100-217.compute-1.amazonaws.com:5432/d9bj3e61otop9n"
engine = create_engine(DATABASE_URL)

TEST_DATABASE_URL = "postgresql://iegxsavpkkbzlf:7bc34cff38335a7e9c09dcde83b44d3ce6cfc903157deba12999d8a7ea58af2f@ec2-3-218-92-146.compute-1.amazonaws.com:5432/d9li5u0oq3rjhe"
test_engine = create_engine(TEST_DATABASE_URL)

Base = declarative_base()


match_players = Table('match_players', Base.metadata,
                        Column('match_id', ForeignKey(
                            'matches.id'), primary_key=True),
                        Column('player_id', ForeignKey(
                            'players.id'), primary_key=True)
                        )


class Match(Base):
    __tablename__ = "matches"
    id = Column(Integer, primary_key=True)
    date = Column(Date, default=func.now())
    white_score = Column(Integer)
    black_score = Column(Integer)
    players = relationship('Player',
                            secondary=match_players,
                            back_populates='matches')


class Player(Base):
    __tablename__ = "players"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    rating = Column(Integer, nullable=False)    
    primary_position = Column(String, nullable=False)
    gk_rating = Column(Integer, nullable=False)    
    dfc_rating = Column(Integer, nullable=False)
    lat_rating = Column(Integer, nullable=False)
    md_rating = Column(Integer, nullable=False)
    ext_rating = Column(Integer, nullable=False)
    del_rating = Column(Integer, nullable=False)
    matches = relationship('Match',
                            secondary=match_players,
                            back_populates='players')


    


