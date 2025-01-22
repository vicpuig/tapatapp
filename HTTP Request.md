# HTTP Request
Un HTTP request és una sol·licitud que un client (normalment un navegador web o una aplicació) envia a un servidor utilitzant el protocol HTTP (HyperText Transfer Protocol). Aquesta sol·licitud permet al client demanar recursos o enviar dades al servidor, com ara pàgines web, imatges o informació per processar.
Components d'una HTTP request
Mètode HTTP: Indica el tipus d'acció que el client vol fer. Els mètodes més comuns són:
GET: Demanar dades o recursos (com una pàgina web).
POST: Enviar dades al servidor (per exemple, formularis).
PUT: Actualitzar recursos existents al servidor.
DELETE: Eliminar un recurs al servidor.
URL (Uniform Resource Locator): Especifica el recurs que es vol accedir o modificar.
Headers: Informació addicional sobre la sol·licitud, com ara el tipus de dades acceptades, l'autenticació, o la configuració de codificació.
Body (opcional): En cas de mètodes com POST o PUT, conté les dades que s'envien al servidor (per exemple, dades de formularis o informació en format JSON).

## 1.1 Exemples de HTTP request
### GET request:
> GET /index.html HTTP/1.1
> Host: www.example.com
### POST request:
> POST /api/login HTTP/1.1
> Host: www.example.com
> Content-Type: application/json
> Content-Length: 45
>
>
> {
>  "username": "usuari",
>  "password": "1234"
> }
### Com funciona un HTTP request en un entorn real?
El client (navegador o aplicació) inicia una sol·licitud HTTP enviant-la a un servidor.
El servidor processa la sol·licitud i respon amb un HTTP response, que pot incloure dades (com una pàgina HTML) o un estat de confirmació (com 200 OK o 404 Not Found).
## 1.2 clients HTTP
curl (acrònim de Client URL) és una eina de línia de comandes utilitzada per transferir dades des d'un client fins a un servidor, o viceversa, a través de diferents protocols de xarxa, com ara HTTP, HTTPS, FTP, SFTP, SMTP, POP3, i molts més.

Instal·lar curl:  https://scoop.sh/#/apps?q=curl

IMPORTANT : heu d’utilitzar la ruta del curl que heu instal·lat amb scoop. A PowerShell, curl és un alias de Invoke-WebRequest i dona error 

Executar una petició GET:

> PS C:\Users\amallad2> C:\Users\amallad2\scoop\apps\curl\current\bin\curl https://proven.cat

Desar la resposta en un fitxer:

> PS C:\Users\amallad2> C:\Users\amallad2\scoop\apps\curl\current\bin\curl -o fitxer.html https://api.chucknorris.io/jokes/random?category=dev

Executar petició POST:  https://www.postman.com/postman/published-postman-templates/documentation/ae2ja6x/postman-echo?ctx=documentation

> PS> C:\Users\amallad2\scoop\apps\curl\current\bin\curl -X POST -H "Content-Type: application/json"  -d "{'test': 'value'}" https://postman-echo.com/post

## 1.3 Mime Types

Els MIME types (Multipurpose Internet Mail Extensions) són estàndards utilitzats per identificar el tipus de contingut d'un fitxer o dades en comunicacions a través d'internet. Originalment, es van crear per correu electrònic, però avui dia s'utilitzen àmpliament en protocols com HTTP per indicar el tipus de contingut d'una resposta o sol·licitud.

### 1. multipart/form-data
multipart/form-data és un tipus de MIME utilitzat principalment per enviar formularis HTML que contenen fitxers o dades binàries (per exemple, imatges, documents, etc.). Aquest tipus de codificació permet enviar diversos tipus de dades (com text i fitxers) en una sola petició HTTP. És el més utilitzat en formularis que permeten la càrrega de fitxers.

Petició Http POST
<form action="https://example.com/upload" method="POST" enctype="multipart/form-data">
    <label for="name">Nom:</label>
    <input type="text" id="name" name="name" value="Joan">
    <br>
    <label for="file">Selecciona una imatge:</label>
    <input type="file" id="file" name="file">
    <br>
    <input type="submit" value="Enviar">
</form>

es genera una petició POST

POST /upload HTTP/1.1
Host: example.com
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Length: 5000


----WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="name"


Joan
----WebKitFormBoundary7MA4YWxkTrZu0gW
Content-Disposition: form-data; name="file"; filename="image.jpg"
Content-Type: image/jpeg


(binary data of the image)
----WebKitFormBoundary7MA4YWxkTrZu0gW--


### 2. application/x-www-form-urlencoded
application/x-www-form-urlencoded és el tipus de codificació per defecte utilitzat quan s’envien dades a través d’un formulari HTML utilitzant el mètode POST (o GET en alguns casos). Les dades s’envien com a una cadena de text amb parelles clau-valor, on les claus i els valors estan separats per = i cada parella es separa per &.

Exemple petició Http  POST:

POST /submit HTTP/1.1
Host: example.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 27


username=John+Doe&age=30&city=New+York


### 3. application/json
application/json és el tipus MIME utilitzat per enviar dades en format JSON. JSON (JavaScript Object Notation) és un format lleuger per emmagatzemar i transportar dades, àmpliament utilitzat en API RESTful i serveis web moderns. Aquest tipus s’utilitza per a la comunicació entre clients i servidors que requereixen enviar dades estructurades de forma més complexa, com objects o arrays.

POST /submit HTTP/1.1
Host: example.com
Content-Type: application/json
Content-Length: 42


{
  "username": "John Doe",
  "age": 30,
  "city": "New York"
}
