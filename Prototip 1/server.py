from flask import Flask, request, jsonify

class User:
    def __init__(self, id, username, password, email):
        self.id=id
        self.username=username
        self.password=password
        self.email=email

    def __str__ (self):
        return "User ID: " + str(self.id) + "| Username: " + self.username

listUsers= [
    User(1, "usuari1", "12345", "prova@gmail.com"),
    User(2,"user2", "123", "user2@proven.cat"),
    User(3,"admin","12","admin@proven.cat")
]

"""for u in listUsers:
    print(u)"""

class DAO_Users:
    def __init__(self):
        self.users=listUsers

    def getUserByUsername(self,username):
        for u in listUsers:
            if (u.username == username):
                return u
        
        else:
            return None
            
daoUser = DAO_Users()

u=daoUser.getUserByUsername("usuari1")
if(u):
    print(u)
else:
    print("Usuari no trobat")
u=daoUser.getUserByUsername("notrobat")

app = Flask(__name__)

@app.route('/llista', methods=['GET'])
def hello():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)

