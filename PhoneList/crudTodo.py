from flask import Flask, jsonify, request, render_template, Response
app = Flask(__name__)

contacts = [{'id': 1, 'name': 'John Doe', 
'phone': '555-555-5555'}]

@app.route('/contactlist',methods=['GET'])
def contactlist():
    return render_template('contactlist.html')

# GET request to retrieve all contacts
@app.route('/contacts', methods=['GET'])
def get_contacts():
    return {'contacts': contacts}

# GET request to retrieve one contacts
@app.route('/contacts/<int:id>', methods=['get'])
def get_contact(id):
    for c in contacts:
        if c['id'] == id:
            contact = c
            return {'contact': contact}
    return Response("Contato inexistente", status=400)

# POST request to add a new contact with data of the new contact on a json file
@app.route('/contacts', methods=['POST'])
def add_contact():
    #id is created here 
    name = request.json['name']
    phone = request.json['phone']
    contact = {
        'id': contacts[-1]["id"] + 1,
        'name': name,
        'phone': phone
    }
    print("AAAA", name)
    print("BBB", phone)
    print("CCC", contact['name'], contact['phone'])
    print("DDD", contact)
    contacts.append(contact)
    return {'contact': contact}

# PUT request to update a contact
@app.route('/contacts/<int:id>', methods=['PUT'])
def update_contact(id):
    print("Printando ID antes dos request.json: ", id)
    print("request.json", request.json)
    name = request.json['name']
    phone = request.json['phone']
    print("Printando ID depois dos request.json: ", id)
    print("name ", name)
    print("phone ", phone)
    for c in contacts:
        if id == c['id']:
            if request.json['name']:
                c['name'] = request.json['name']
            elif request.json['phone']:
                c['phone'] = request.json['phone']
        updated_contact = c
        
        return {'contact': updated_contact}
    return Response("Contato inexistente", status=400)

# DELETE request to delete a contact
@app.route('/contacts/<int:id>', methods=['DELETE'])
def delete_contact(id):
    return {'message': ''}


app.run(debug=True,port = 5001)
