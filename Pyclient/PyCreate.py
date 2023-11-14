# A demo python web client

import requests

endpoint = 'http://localhost:8000/api/products/'

data = {
    'title':'Newly Created again'
}

response = requests.post(endpoint, json=data)
print(response.status_code)
# print(response.text)
print(response.json())
