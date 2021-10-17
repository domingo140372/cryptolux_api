#from urllib2 import Request, urlopen
import requests
import json

values = """
  {
    "username": "usuario@api.com",
    "access_key": "NWNmMTczNGYtZjQ0OS00MjgwLTg51WItYjNiNWRiNGUxMjIzOnM/WDkqPypfVFN="
  }
"""

headers = {
  'Content-Type': 'application/json'
}
respuesta = requests.get('https://api.siigo.com/auth', data=values, headers=headers)

response_body = respuesta.json()
print(response_body)