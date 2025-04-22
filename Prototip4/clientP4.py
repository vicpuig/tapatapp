import requests
from dadesServer import User, Child, Tap

# ---- LOGIN ----
class DAOUser:
    token = None # Variable per emmagatzemar el token d'autentificació

    def getUserByCredentials(username, password):
        payload = {'username': username, 'password': password} # Creo un diccionari amb les dades del user que vull obtenir
        headers = {"Content-Type": "application/json"} # Creo un diccionari amb les capçaleres de la petició HTTP
        responseGetUser = requests.post('http://localhost:10050/prototip3/login/', json=payload, headers=headers)  
        
        if responseGetUser.status_code == 200: # Si la resposta es existosa, es converteix les dades del user que envia el server a format JSON i es guarden en la variable userData
            responseData = responseGetUser.json()
            DAOUser.token = responseData['token'] # Guardo el token d'autentificació en la variable token de la classe DAOUser
            userData = responseData['user']
            user = User(userData['id'], userData['username'], userData['password'], userData['email']) # Amb les dades extretes, es crea un usuari i es retorna 
            return user
        else:
            return None            

class LoginView: 
    def __init__(self, username, password):
        self.username=username
        self.password=password

    # getters dels credencials per consola
    def getUsernameByConsole():
        username = str(input("👤 Introdueixi el seu username: "))
        return username
    def getPasswordByConsole():
        password = str(input("🔐 Introdueixi el seu password: "))
        return password

    # showInfo del user dels credencials. No només printea, també retorna el user per així poder guardar la id al main com a token d'autentificació un cop fet el login   
    def showUserInfo(username, password):
        user = DAOUser.getUserByCredentials(username, password)
        if (user):
            print("\nInici de sessió correcte! ✅\n")
            print("👩‍ --- User info --- 👨")
            print(f"   👤 Username: {user.username}")
            print(f"   📑 Password: {user.password}")
            print(f"   📧 Email: {user.email}")
            return user
        else:
            print("❌ ERROR: Credencials incorrectes")
            print()
            return None

# ---- CHILD & TAPS----
class DAOChild:
    def getChildByUser(user_id):
        headers = {"Authorization": DAOUser.token} # Envio el token en els headers
        #faig petició al endpoint per cridar el getChildByUser del server, aconseguir les dades del Child i guardar-les en un response
        responseGetChild = requests.get(f'http://localhost:10050/prototip3/children/{user_id}', headers=headers) 

        #Si el response és exitós, converteixo les dades obtingudes en format json i les guardo en una llista de diccionaris "children" utilitzant un list comprehension, on cada diccionari tindrà les dades d'un child
        if responseGetChild.status_code == 200:
            childrenData = responseGetChild.json()
            children = [
                Child(
                    id=child["id"],
                    child_name=child["child_name"],
                    sleep_average=child.get("sleep_average", 0),  #default 0 per si no está en el JSON
                    treatment_id=child.get("treatment_id", None),
                    time=child.get("time", 0)
                ) for child in childrenData
            ]
            return children

    def getAllTaps(child_id):
        headers = {"Authorization": DAOUser.token}
        responseGetAllTaps = requests.get(f'http://localhost:10050/prototip3/taps/{child_id}', headers=headers)

        if responseGetAllTaps.status_code == 200:
            allTapsData = responseGetAllTaps.json()
            taps = [
                Tap(
                    id = tap["id"],
                    child_id = tap["child_id"],
                    status_id = tap["status_id"],
                    user_id = tap["user_id"],
                    init = tap["init"],
                    end = tap["end"]
                ) for tap in allTapsData
            ]
            return taps

class ChildrenView:
    def showChildInfo(user_id):
        children = DAOChild.getChildByUser(user_id)
        if children:
            print("\n🚼 --- Children info --- 🚼")
            child_ids = []
            for child in children:
                print(f"   🆔 ID: {child.id}")
                print(f"   👶 Nombre: {child.child_name}")
                print(f"   💤 Mediana de sueño: {child.sleep_average}")
                print()
                child_ids.append(child.id)
            return child_ids
        else:
            print("⚠️ ERROR: Child not found\n")
            print()
            return None

class TapView:
    def showAllTaps(child_id):
        taps = DAOChild.getAllTaps(child_id)
        if taps:
           for tap in taps:
               print(f"👀 --- Tap #{tap.id} info --- 👀")
               print(f"   🔹 Tap ID: {tap.id}")
               print(f"   👶 Child ID: {tap.child_id}")
               print(f"   🔍 Estado: {tap.status_id}")
               print(f"   ⏳ Inici: {tap.init}")
               print(f"   ⌛ Final: {tap.end}")
               print()
        else:
            print("⚠️ ERROR: Taps not found\n")

# ---- MAIN ----
if __name__ == "__main__":
    username = LoginView.getUsernameByConsole()
    password = LoginView.getPasswordByConsole()
    user = LoginView.showUserInfo(username, password)

    if user:
        user_id_token = user.id
    else:
        exit()
    
    child_ids_tokens = ChildrenView.showChildInfo(user_id_token)
    if child_ids_tokens:
        for child_id in child_ids_tokens:
            TapView.showAllTaps(child_id)
    else:
        exit()
    