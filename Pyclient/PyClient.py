# A demo python web client

import requests

endpoint = 'http://localhost:8000/api/products/1'

response = requests.get(endpoint)
print(response.status_code)
# print(response.text)
print(response.json())
