import dadesServer as server
from dadesServer import User, Child, Tap, Role, Status, Treatment
from flask import Flask, request, jsonify

#Comprovació de la funcionalitat de la creació de Users
newUser = User(id=1, username="New Test", password="12345", email="newuserprova@gmail.com")
print(newUser)

#Comprovació de la funcionalitat de la userList
for user in server.users:
    print(user)

#Classes DAO
class DAOUser:
    def __init__(self):
        self.listUsers = server.users

    def getUserByCredentials(self, username, password):
        for user in self.listUsers:
            if (username == user.username and password == user.password): 
                return user
            
        return None



class DAOChild:
    pass

class DAOTap:
    pass 



