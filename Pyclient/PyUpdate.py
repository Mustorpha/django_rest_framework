# A demo python web client

import requests

endpoint = 'http://localhost:8000/api/products/1/update'

data = {
    'title':'updated using http put',
    'price':50.67
}

response = requests.put(endpoint, json=data)
print(response.status_code)
# print(response.text)
print(response.json())
