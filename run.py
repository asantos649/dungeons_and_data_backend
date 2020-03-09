from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Character import Base, Character

app = Flask(__name__)
CORS(app)

engine = create_engine('sqlite:///characters.db')

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
        response =  jsonify(characters)

    if (request.method == 'POST'):
        data = request.get_json()
        char = Character(**data)
        session.add(char)

        response = jsonify(clean_char(char))

    session.commit()
    return response