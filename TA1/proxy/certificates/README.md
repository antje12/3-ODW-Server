openssl genrsa -des3 -out rootCA.key 2048
openssl req -x509 -new -nodes -key rootCA.key -sha256 -days 1024 -out rootCA.pem

openssl req -new -sha256 -nodes -out server.csr -newkey rsa:2048 -keyout site.key
openssl x509 -req -in server.csr -CA rootCA.pem -CAkey rootCA.key -CAcreateserial -out site.crt -days 1000 -sha256 -extfile v3.ext
