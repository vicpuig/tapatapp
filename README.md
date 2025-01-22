# Tapatapp
---
[Descripció del Projecte](descTapatApp.md)

[Requeriments Tècnics](requerimentsTecnics.md)

## Prototip 1:
[Diagrama Prototip 1](diagramaPrototip.mermaid)

### Definició dels EndPoint
- Descripció: Servei que consulta un User per Username
- End-point: /prototip/getuser
- Method: GET
- Parametres: username
- Resposta:
- Code 200 Ok: {id=1,"username:"user1","password:"123456","email:"mail@gmail.com"}
- Code 400 No trobat: {"error":"No trobat"}
