import mysql.connector
from flask import Flask, request, jsonify
import secrets

app = Flask(__name__)

# Configuración de la conexión a la base de datos
db_config = {
    "host": "localhost",
    "user": "tu_usuario",
    "password": "tu_contraseña",
    "database": "tu_base_de_datos"
}

# Diccionario para almacenar los tokens generados
auth_tokens = {}

# Clases DAO
class DAO_User:
    def __init__(self):
        self.connection = mysql.connector.connect(**db_config)

    def getUserByCredentials(self, username, password):
        cursor = self.connection.cursor(dictionary=True)
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()
        cursor.close()
        return user

class DAO_Child:
    def __init__(self):
        self.connection = mysql.connector.connect(**db_config)

    def getChildByUser(self, user_id):
        cursor = self.connection.cursor(dictionary=True)
        query = """
            SELECT c.* FROM children c
            JOIN relation_user_child r ON c.id = r.child_id
            WHERE r.user_id = %s
        """
        cursor.execute(query, (user_id,))
        children = cursor.fetchall()
        cursor.close()
        return children

    def getAllTaps(self, child_id):
        cursor = self.connection.cursor(dictionary=True)
        query = "SELECT * FROM taps WHERE child_id = %s"
        cursor.execute(query, (child_id,))
        taps = cursor.fetchall()
        cursor.close()
        return taps

DAOUser = DAO_User()
DAOChild = DAO_Child()

@app.route("/prototip3/login/", methods=["POST"])
def login():
    try:
        data = request.json
        username = data.get("username")
        password = data.get("password")

        user = DAOUser.getUserByCredentials(username, password)

        if user:
            token = secrets.token_hex(32)
            auth_tokens[token] = user["id"]
            return jsonify({"token": token, "user": user}), 200
        else:
            return jsonify({"error": "Credenciales incorrectas."}), 404
    except Exception as e:
        return jsonify({"error": "Error inesperado del sistema", "detalles": str(e)}), 500

# Middleware para verificar el token
def token_required(f):
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token or token not in auth_tokens:
            return jsonify({"error": "Token de autenticación inválido o no proporcionado"}), 401
        return f(*args, **kwargs)
    wrapper.__name__ = f.__name__
    return wrapper

@app.route('/prototip3/children/', defaults={'user_id': None}, methods=['GET'])
@app.route("/prototip3/children/<int:user_id>", methods=["GET"])
@token_required
def getChildByUser(user_id):
    if user_id is None:
        return jsonify({"error": "No se ha introducido ningún parámetro"}), 400

    children = DAOChild.getChildByUser(user_id)

    if children:
        return jsonify(children), 200
    else:
        return jsonify({"error": "Este usuario no tiene ningún niño a su cargo"}), 404

@app.route('/prototip3/taps/', defaults={'child_id': None}, methods=['GET'])
@app.route("/prototip3/taps/<int:child_id>", methods=['GET'])
@token_required
def getAllTaps(child_id):
    if child_id is None:
        return jsonify({"error": "No se ha introducido ningún parámetro"}), 400

    taps = DAOChild.getAllTaps(child_id)

    if taps:
        return jsonify(taps), 200
    else:
        return jsonify({"error": "Este niño no tiene ningún tap registrado"}), 404

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="10050")