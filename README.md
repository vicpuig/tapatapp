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
| Descripció  | End-point     | Method     |Tipus de petició|Parametres| resposta|
| :---        |  :---        |  :---        |  :---         |  :---     |  :--- | 
| Servei que consulta un User per Username | /prototip/getuser | GET | application/json  | username |  {"id":1, "email":"victor@gmail.com", "username":"usuari1", "password":"12345"}      |
