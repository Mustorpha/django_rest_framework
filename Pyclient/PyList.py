# A demo python web client

import requests
from getpass import getpass

endpoint = 'http://localhost:8000/api/auth/'

password = getpass()
auth_response = requests.post(endpoint, json={'username':'Mustorpha', 'password':password})
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        'Authorization':f'Bearer {token}'
        }
    endpoint = 'http://localhost:8000/api/products/'

    response = requests.get(endpoint, headers=headers)
    print(response.status_code)
    # print(response.text)
    print(response.json())
