import requests 

class User:
    def __init__(self, id, username, password, email):
        self.id=id
        self.username=username
        self.password=password
        self.email=email

    def __str__ (self):
        return "User ID: " + str(self.id) + "| Username: " + self.username
    
class Error:
    def __init__(self, code, description):
        self.code=code
        self.description=description

    def __str__ (self):
        return "Error Code: " + str(self.code) + "| Description: " + self.description
    
class DAOUser:
    def getUserByUsername(username):
        response = requests.get(f'http://localhost:10050/prototip1/getuser?username={username}')  # El DAO rep el username i fa una Request HTTP de tipus GET al endpoint indicat
        
        if response.status_code == 200: # Si la resposta es existosa, es converteix les dades del user que envia el server a format JSON i es guarden en la variable userData
            userData = response.json()
            user = User(userData['id'], userData['username'], userData['password'], userData['email']) # Amb les dades extretes, es crea un usuari i es retorna 
            return user
        else:
            return None

class View: 
    def __init__(self, username):
        self.username=username
    
    def getUsernameByConsole():
        username = str(input("Enter username: "))
        return username

    def showUserData(user):
        user = DAOUser.getUserByUsername(user)
        if (user):
            print("*--- User info ---*")
            print(user.__str__)
        else:
            print("ERROR: User not found")
    
    # def showErrorData(error):
    #    return error

















