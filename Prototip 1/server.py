from flask import Flask, request, jsonify

app = Flask(__name__)

# Classe User
class User:
    def __init__(self, id, username, password, email):
        self.id=id
        self.username=username
        self.password=password
        self.email=email

    def __str__ (self):
        return "User ID: " + str(self.id) + " | Username: " + self.username + " | Email: " + self.email

# Dades d'exemple
listUsers= [
    User(1, "usuari1", "12345", "victor@gmail.com"),
    User(2,"user2", "123", "user2@proven.cat"),
    User(3,"admin","12","admin@proven.cat")
]

# Classes DAO
class DAO_Users:
    def __init__(self):
        self.users=listUsers

    def getUserByUsername(self,username):
        for u in listUsers:
            if (u.username == username):
                return u
        return None

# Inicialitzar DAOs            
daoUser = DAO_Users()
#print(daoUser.getUserByUsername("usuari1"))


# Rutes del Servei Web
# --------------------
 
#http://192.168.144.176:10050/prototip/getuser/{string:username}

@app.route('/prototip/getuser/', defaults={'username': None}, methods=['GET'])
@app.route('/prototip/getuser/<string:username>', methods=['GET'])
def prototipGetUser(username):
    try: 
        if username is None: 
            return jsonify({"error": "Parametre no introduit"}), 400
        
        user = daoUser.getUserByUsername(username)
        
        if user: 
            return jsonify(user.__dict__), 200
        else: 
            return jsonify({"error": f"Usuari {username} no trobat"}), 404
    except Exception as e:
        return jsonify({"error": "Error inesperat","detalls":str(e)}), 500
        
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="10050")

"""
# http://192.168.144.176:10050/prototip/getuser?name=Víctor&email=victor@gmail.com

@app.route('/prototip/getuser', methods=['GET'])
def getuser():
    name=str(request.args.get('name'))
    email = str(request.args.get('email'))
    return "Nom: " + name + " | Email: " + email
"""