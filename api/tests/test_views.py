from .test_setup import TestSetUp

class TestApi(TestSetUp):
    
    def test_unauthenticated_request(self):
        response = self.client.get(self.product_list)
        self.assertEqual(response.status_code, 403)

    def test_authenticated_request(self):
        endpoint = self.auth_token
        auth_response = self.client.post(endpoint, json={'username':'Mustorpha', 'password':'Zyper2468'})
        self.assertEqual(auth_response.status_code, 200)

        if auth_response.status_code == 200:
            token = auth_response.json()['token']
            headers = {
                'Authorization':f'Bearer {token}'
                }
            endpoint = self.product_list
            response = self.client.get(endpoint, headers=headers)
            self.asserEqual(response.status_code, 200)