from flask import Flask, jsonify, request, render_template, Response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///contacts.sqlite3"

db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String)
    phone = db.Column(db.String)

contacts = [{'id': 1, 'name': 'Teste', 
'phone': '9999'}]

@app.route('/contactlist',methods=['GET'])
def contactlist():
    return render_template('contactlist.html')

# GET request to retrieve all contacts
@app.route('/contacts', methods=['GET'])
def get_contacts():
    if not contacts:
        return jsonify({'message:':'No contacts found in the server'}), 404
    return jsonify({'contacts': contacts}), 200

# GET request to retrieve one contacts
@app.route('/contacts/<int:id>', methods=['get'])
def get_contact(id):
    for contact in contacts:
        if contact['id'] == id:
            return jsonify({'contact': contact}), 200
    return jsonify({'message:':'Contact not found'}), 404

# POST request to add a new contact with data of the new contact on a json file
@app.route('/contacts', methods=['POST'])
def add_contact():
    if not request.is_json: 
        return jsonify({'message':'body is not a json'}), 415
    data = request.get_json()
    if not data or not all(key in data for key in ('name', 'phone')):
        return jsonify({'message','bad request'}), 400
    id = 1
    if len(contacts) > 0:
        id = contacts[-1]["id"] + 1
    contact = {
        'id': id,
        'name': data['name'],
        'phone': data['phone']
    }
    contacts.append(contact)
    return jsonify({'contact': contact}), 201

# PUT request to update a contact
@app.route('/contacts/<int:id>', methods=['PUT'])
def update_contact(id):
    if not request.is_json: 
        return jsonify({'message':'body is not a json'}), 415
    data = request.get_json()
    if not data or not all(key in data for key in ('name', 'phone')):
        return jsonify({'message','bad request'}), 400
    for contact in contacts:
        if id == contact['id']:
            contact['name'] = data['name']
            contact['phone'] = data['phone']
            return jsonify({'contact': contact}), 200
    return jsonify({'message':'Contact not found'}), 404

# DELETE request to delete a contact
@app.route('/contacts/<int:id>', methods=['DELETE'])
def delete_contact(id):
    for i,contact in enumerate(contacts):
        if id == contact['id']:
            del contacts[i]
            return jsonify({'message':'Contact deleted'}), 200
    return {'message': ''}

db.create_all()
db.init_app(app)
app.run(debug=True,port = 5001)