# A demo python web client

import requests

endpoint = 'http://localhost:8000/api/products/6/delete'

response = requests.delete(endpoint)
print(response.status_code)
# print(response.text)
# print(response.json())
