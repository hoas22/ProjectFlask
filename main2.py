from flask import Flask, request

app = Flask(__name__)


users = [
    {
        "id": 1,
        "name": "moises",
        "age": 22
    },
    {
        "id": 2,
        "name": "jesus",
        "age": 23
    }
]


# # Decoradores
# @app.route('/')
# def inicio():
#     return {
#         "message": "hola mundo"
#     }
@app.route('/users', methods=['GET'])
def userList():
    return users, 200


@app.route('/users/<int:id>', methods=['GET'])
def userGetById(id):
    for user in users:
        if user['id'] == id:
            return user, 200

    return {
        "message": f'User ID-> {id} , not found'
    }, 404


@app.route('/users', methods=['POST'])
def userCreate():
    data = request.get_json()
    users.append(data)
    return {
        "message": 'user create',
        "data": users
    }, 200


@app.route('/users/<int:id>', methods=['PUT'])
def userByIdUpdate(id):
    for user in users:
        if user['id'] == id:
            data = request.get_json()
            user['name'] = data['name']
            user['age'] = data['age']
            return user, 200

    return {
        "message": f'User ID-> {id} , not found'
    }, 404
