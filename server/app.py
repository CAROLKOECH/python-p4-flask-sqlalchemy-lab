#!/usr/bin/env python3

from flask import Flask, make_response
from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = Animal.query.get(id)
    if not animal:
        response_body = '<h1>404 Animal not found</h1>'
        response = make_response(response_body, 404)
        return response

    response_body = f'<h1>Information for {animal.name}</h1>'
    response_body += f'<ul><li>Species: {animal.species}</li>'
    response_body += f'<li>Zookeeper: {animal.zookeeper.name}</li>'
    response_body += f'<li>Enclosure: {animal.enclosure.environment}</li></ul>'

    response = make_response(response_body, 200)
    return response

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.get(id)
    if not zookeeper:
        response_body = '<h1>404 Zookeeper not found</h1>'
        response = make_response(response_body, 404)
        return response

    response_body = f'<h1>Information for {zookeeper.name}</h1>'
    response_body += f'<ul><li>Birthday: {zookeeper.birthday}</li>'
    response_body += '<li>Animals:</li><ul>'
    for animal in zookeeper.animals:
        response_body += f'<li>{animal.name} ({animal.species})</li>'
    response_body += '</ul></ul>'

    response = make_response(response_body, 200)
    return response

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.get(id)
    if not enclosure:
        response_body = '<h1>404 Enclosure not found</h1>'
        response = make_response(response_body, 404)
        return response

    response_body = f'<h1>Information for Enclosure</h1>'
    response_body += f'<ul><li>Environment: {enclosure.environment}</li>'
    response_body += f'<li>Open to Visitors: {enclosure.open_to_visitors}</li>'
    response_body += '<li>Animals:</li><ul>'
    for animal in enclosure.animals:
        response_body += f'<li>{animal.name} ({animal.species})</li>'
    response_body += '</ul></ul>'

    response = make_response(response_body, 200)
    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)
