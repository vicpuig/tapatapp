# Dades d'exemple amb List
# Clase User
class User:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
    
    def __str__(self):
        return self.username + ":" + self.password + ":" + self.email
    

users = [
    User(id=1, username="mare", password="12345", email="prova@gmail.com"),
    User(id=2, username="pare", password="123", email="prova2@gmail.com")
]

# Crear les classes Child, Tap, Role, Status i Treatment

class Child: 
    def __init__(self, id, child_name, sleep_average, treatment_id, time):
        self.id = id
        self.child_name = child_name
        self.sleep_average = sleep_average
        self.treatment_id = treatment_id
        self.time = time
    
    def __str__(self): 
        return self.id + ":" + self.child_name + ":" + self.sleep_average + ":" + self.treatment_id + ":" + self.time

children = [
    Child(id=1, child_name="Carol Child", sleep_average=8, treatment_id=1, time=6),
    Child(id=2, child_name="Jaco Child", sleep_average=10, treatment_id=2, time=6),
    Child(id=3, child_name="Carol Child 2", sleep_average=6, treatment_id=1, time=5)
]

class Tap:
    def __init__(self, id, child_id, status_id, user_id, init, end):
        self.id = id
        self.child_id = child_id
        self.status_id = status_id
        self.user_id = user_id
        self.init = init
        self.end = end
    
    def __str__(self):
        return self.id + ":" + self.child_id + ":" + self.status_id + ":" + self.user_id + ":" + self.init + ":" + self.end
        
taps = [
    Tap(id=1, child_id=1, status_id=1, user_id=1, init="2024-12-18T19:42:43", end="2024-12-18T20:42:43"),
    Tap(id=2, child_id=3, status_id=2, user_id=2, init="2024-12-18T21:42:43", end="2024-12-18T22:42:43")
]

relation_user_child = [
    {"user_id": 1, "child_id": 1, "rol_id": 1},
    {"user_id": 1, "child_id": 1, "rol_id": 2},
    {"user_id": 2, "child_id": 2, "rol_id": 1},
    {"user_id": 2, "child_id": 2, "rol_id": 2},
    {"user_id": 1, "child_id": 3, "rol_id": 2}
]

class Role:
    def __init__(self, id, type_rol):
        self.id = id
        self.type_rol = type_rol

    def __str__(self):
        return self.id + ":" + self.type_rol

roles = [
    Role(id=1, type_rol='Admin'),
    Role(id=2, type_rol='Tutor Mare Pare'),
    Role(id=3, type_rol='Cuidador'),
    Role(id=4, type_rol='Seguiment')
]

class Status:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return self.id + ":" + self.name

statuses = [
    Status(id=1, name="sleep"),
    Status(id=2, name="awake"),
    Status(id=3, name="yes_eyepatch"),
    Status(id=4, name="no_eyepatch")
]

class Treatment: 
    def __init__(self, id, name):
        self.id = id
        self.name = name 
    
    def __str__(self):
        return self.id + ":" + self.name

treatments = [
    Treatment(id=1, name='Hour'),
    Treatment(id=2, name='percentage')
]
