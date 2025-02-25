# Tapatapp
---
[Descripció del Projecte](descTapatApp.md)

[Requeriments Tècnics](requerimentsTecnics.md)

## Prototip 1:
[Diagrama Prototip 1](charts/diagramaPrototip.mermaid)

---

[HTTP Request](HTTPRequest.md)

[HTTP Response](HTTPResponse.md)

### Definició dels EndPoint
| Descripció  | End-point     | Method     |Tipus de petició|Parametres|
| :---        |  :---        |  :---        |  :---         |  :---     | 
| Servei que consulta un User per Username | /prototip/getuser | GET | application/json  | username |  

- Code 200 Ok: {"id":1, "email":"victor@gmail.com", "username":"usuari1", "password":"12345"} <br>
- Code 400 No trobat: {"error":"No trobat"} -> Quan no introdueixes cap parametre. <br>
- Code 404 No trobat: {"error":"No trobat"} -> Quan introdueixes un usuername que no correspon als de la llisa d'Usuaris <br>
- Code 500 Error de server: {"error": "Error inesperat","detalls":str(e)} -> Quan peta el servidor <br>
