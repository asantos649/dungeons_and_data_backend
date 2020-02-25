from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Character import Base, Character


# create engine and setup session

engine = create_engine('sqlite:///character.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


# delete all existing rows in character database

session.query(Character).delete()


# add characters for seed data

Char1 = Character(name='Quanjin Yewroot', charClass= 'Druid', race= 'Forest Gnome')
Char2 = Character(name='Braum Silverhammer', charClass= 'Paladin', race= 'Human')

session.bulk_save_objects([Char1, Char2])


# commit to db

session.commit()