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
- Descripció: Servei que consulta un User per Username
- End-point: /prototip/getuser
- Method: GET
- Parametres: username
- Resposta: <br>
    Code 200 Ok: {id=1,"username:"user1","password:"123456","email:"mail@gmail.com"} <br>
    Code 400 No trobat: {"error":"No trobat"}
