from flask import Flask, request, json
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)

    def __init__(self, name):
        self.name = name


class PersonSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('name',)


person_schema = PersonSchema()
person_schema = PersonSchema(many=True)


# endpoint to create new person
@app.route("/name", methods=["POST"])
def add_person():
    name = request.json['name']
    
    new_person = Person(name)

    db.session.add(new_person)
    db.session.commit()

    return f'\n{new_person.name} created\n'


# endpoint to show all people
@app.route("/name", methods=["GET"])
def get_person():
    all_people = Person.query.all()
    result = person_schema.dump(all_people)
    return str(result)


# endpoint to get person detail by id
@app.route("/name/<id>", methods=["GET"])
def person_detail(id):
    person = Person.query.get(id)
    return '\n'+person.name+'\n'


# endpoint to update person
@app.route("/name/<id>", methods=["PUT"])
def person_update(id):
    person = Person.query.get(id)
    name = request.json['name']
    person.name = name
    db.session.commit()
    return f'\n{id} updated to {person.name}'


# endpoint to delete user
@app.route("/name/<id>", methods=["DELETE"])
def person_delete(id):
    person = Person.query.get(id)
    name = person.name
    db.session.delete(person)
    db.session.commit()

    return f'\n{name} was deleted\n'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
