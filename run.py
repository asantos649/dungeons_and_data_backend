from flask import Flask, request, jsonify

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Character import Base, Character

app = Flask(__name__)


engine = create_engine('sqlite:///character.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

@app.route('/api/characters', methods=['GET','POST'])
def character():
    def clean_char(char):
        temp = char.__dict__
        del temp['_sa_instance_state']
        return temp

    if (request.method == 'GET'):
        characters = map(lambda x: clean_char(x), session.query(Character).all())
        return jsonify(characters)

    if (request.method == 'POST'):
        data = request.get_json()
        char = Character(name=data['name'], charClass= data['class'], race= data['race'])
        session.add(char)
        return jsonify(clean_char(char))

    session.commit()