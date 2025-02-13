from flask import Flask, jsonify
from flask import request

app = Flask(__name__)


todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False },
    { "label": "My third task", "done": True },
    { "label": "My fourth task", "done": False },
    { "label": "My fifth task", "done": False }
]

#-------------------GET-------------------

@app.route('/todos', methods=['GET'])
def get_todos():
    json_text = jsonify(todos)
    return json_text

#-------------------POST-------------------

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json#obtiene el body de la peticion
    request.get_json(force=True)
    print("Incoming request with the following body", request_body)#imprime el body de la peticion para verificar que se recibio a modo de depuracion
    todos.append(request_body)# este es el body que se envia en el postman
    return jsonify(todos)#devuelve la lista de todos

#-------------------DELETE-------------------

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if 0 <= position < len(todos):#verifica que la posicion sea valida y que no sea mayor a la longitud de la lista
        del todos[position]  # Elimina el todo en la posición especificada
        return jsonify(todos)  # Devuelve la lista actualizada todos
    else:
        return jsonify({"error": "Invalid position"}), 404  # Devuelve un error 404 si la posición no es válida

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)