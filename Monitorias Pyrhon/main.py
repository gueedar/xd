from flask import Flask, jsonify, request

app = Flask(__name__)

'''
GET -> obtener informacion
POST -> Crear informacion
PUT -> Actualizar informacion
DELETE -> Borrar info
'''

@app.route("/users/<user_id>")

def get_user(user_id):
    user = {"id": user_id, "name": "test", "telefono": "3197237912"}

    #/users/2654?querry=querry_test
    querry = request.args.get("querry")
    if querry:
        user["querry"] = querry
    return jsonify(user), 200

@app.route('/users', methods=['POST'])

def create_user():
    data = request.get_json()
    data["status"] = "Usuario_Creado"
    return jsonify(data), 201

def root():
    return 'Home'

if __name__ == '__main__':
    app.run(debug=True)