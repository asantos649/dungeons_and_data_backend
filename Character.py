from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()

engine = create_engine('sqlite:///character.db')


class Character(Base):
    __tablename__ = 'character'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    charClass = Column(String(250), nullable=False)
    race = Column(String(250), nullable=False)



Base.metadata.create_all(engine)