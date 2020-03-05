from sqlalchemy import Column, ForeignKey, Integer, String, Text

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()

engine = create_engine('sqlite:///characters.db')


class Character(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    charClass = Column(String(250), nullable=False)
    path = Column(String(250))
    race = Column(String(250), nullable=False)
    level = Column(Integer)
    alignment = Column(String(50))
    img_url = Column(String(250))
    status = Column(String(50))
    bio = Column(Text)
    char_strengths = Column(Text)
    flaws = Column(Text)
    strength = Column(Integer)
    constitution = Column(Integer)
    dexterity = Column(Integer)
    wisdom = Column(Integer)
    intelligence = Column(Integer)
    charisma = Column(Integer)
    ability_spells = Column(Text)
    proficiencies = Column(Text)
    equipment = Column(Text)
    attacks = Column(Text)



Base.metadata.create_all(engine)