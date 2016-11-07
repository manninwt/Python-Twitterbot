import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Trump(Base):
    __tablename__ = 'trump'
    id = Column(Integer, primary_key=True)
    topics = Column(String(250), nullable=False)
    statements = Column(String(250), nullable=False)

class Random(Base):
    __tablename__ = 'random'
    id = Column(Integer, primary_key=True)
    topics = Column(String(250), nullable=False)
    statements = Column(String(250), nullable=False)

# I only add this for you Braden
class Anime(Base):
    __tablename__ = 'anime'
    id = Column(Integer, primary_key=True)
    topics = Column(String(250), nullable=False)
    statements = Column(String(250), nullable=False)

class Meme(Base):
    __tablename__= 'meme'
    id = Column(Integer, primary_key=True)
    topics = Column(String(250), nullable=False)
    statements = Column(String(250), nullable=False)

engine = create_engine('sqlite:///sqlalchemy_twitter_bot.db')

Base.metadata.create_all(engine)
