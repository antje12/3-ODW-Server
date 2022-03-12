import json
import requests_unixsocket

session = requests_unixsocket.Session()

response = session.get('http+unix://%2Fvar%2Frun%2Fdocker.sock/containers/json')

responsejson = response.json()

print(json.dumps(responsejson, indent=4))
