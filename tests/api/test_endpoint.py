import requests


class TestApi:
    headers = {'Authorization': 'Token 33c4232f10ac01c06f492f18d7f208eb5aaf2bd0'}
    url = ['http://127.0.0.1:8000/api/v1/coordenadas/atual/', 'http://127.0.0.1:8000/api/v1/coordenadas/start/',
           'http://127.0.0.1:8000/api/v1/coordenadas/movement/']

    def test_get_atual_status_code(self):
        resp = requests.get(url=self.url[0], headers=self.headers)
        assert resp.status_code == 200

    def test_post_start_status_code(self):
        resp = requests.post(url=self.url[1], headers=self.headers, data="")
        assert resp.status_code == 201

    def test_post_movement_status_code(self):
        movimento = {
            "movimentos": ["ge", "m", "m", "Gd", "M"]
        }
        resp = requests.post(url=self.url[2], headers=self.headers, data=movimento)
        assert resp.status_code == 201
