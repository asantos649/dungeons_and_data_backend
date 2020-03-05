from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Character import Base, Character


# create engine and setup session

engine = create_engine('sqlite:///characters.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


# delete all existing rows in character database

session.query(Character).delete()


# add characters for seed data

Char1 = Character(
    name = 'TestString',
    charClass = 'TestString',
    path = 'TestString',
    race = 'TestString',
    level = 10,
    alignment = 'TestString',
    img_url = 'TestString',
    status = 'TestString',
    bio = 'Column(Text)',
    char_strengths = 'Column(Text)',
    flaws = 'Column(Text)',
    strength = 10,
    constitution = 10,
    dexterity = 10,
    wisdom = 10,
    intelligence = 10,
    charisma = 10,
    ability_spells = 'Column(Text)',
    proficiencies = 'Column(Text)',
    equipment = 'Column(Text)',
    attacks = 'Column(Text)'
    )
Char2 = Character(
    name = 'TestString',
    charClass = 'TestString',
    path = 'TestString',
    race = 'TestString',
    level = 10,
    alignment = 'TestString',
    img_url = 'TestString',
    status = 'TestString',
    bio = 'Column(Text)',
    char_strengths = 'Column(Text)',
    flaws = 'Column(Text)',
    strength = 10,
    constitution = 10,
    dexterity = 10,
    wisdom = 10,
    intelligence = 10,
    charisma = 10,
    ability_spells = 'Column(Text)',
    proficiencies = 'Column(Text)',
    equipment = 'Column(Text)',
    attacks = 'Column(Text)'
    )
# Char2 = Character(name='Braum Silverhammer', charClass= 'Paladin', race= 'Human')

session.bulk_save_objects([Char1,Char2])


# commit to db

session.commit()