import requests
from getpass import getpass

username = input('Enter username\n')
password = getpass('Enter password\n')

endpoint = "http://localhost:8000/api/auth/"


auth_response = requests.post(endpoint, json={'username':username, 'password': password})
print(auth_response.json())

if auth_response.status_code == 200:
  token = auth_response.json()['token']
  headers = {
    "Authorization": f"Bearer {token}"
  }
  endpoint = "http://localhost:8000/api/products/"

  response_get = requests.get(endpoint, headers=headers)
  print(response_get.json())
