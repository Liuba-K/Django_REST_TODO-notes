import requests
from requests.auth import HTTPBasicAuth
import time

DOMAIN = 'http://127.0.0.1:8000'


def timeout():
    time.sleep(2)


def get_url(url):
    return f'{DOMAIN}{url}'

"""#test 1_list user
auth = HTTPBasicAuth(username='liuba', password='1')
response = requests.get('http://127.0.0.1:8000/api/users/', auth=auth)
print(response.json())

#test 2
data = {'username':'liuba', 'password':'1'}
response = requests.post('http://127.0.0.1:8000/api-token-auth/', data=data)
token = response.json().get('token')
response_tok = requests.get('http://127.0.0.1:8000/api/projects/', headers={'Authorization':f'Token {token}'})
print(response_tok.json())


timeout()

#не авторизован
response = requests.get(get_url('/api/users/'))
assert response.status_code == 401
"""

timeout()
#базова авторизация
response =requests.get(get_url('/api/users/'), auth=('liuba', '1'))
assert response.status_code == 200

timeout()
#авторизация по токену
TOKEN = requests.post(get_url('/api-token-auth/'), data={'username':'liuba', 'password':'1'}).json().get('token')
headers = {'Authorization': f'Token {TOKEN}'}
response = requests.get(get_url('/api/users/'), headers=headers)
assert response.status_code == 200

timeout()
#авторизация по jwt
response = requests.post(get_url('/api/token/'), data={'username': 'liuba', 'password': '1'})
result = response.json()
access = result['access']
print('first token', access, end=f'\n{50*"*"}\n')
refresh = result['refresh']
print('refresh', refresh, end=f'\n{50*"*"}\n')

headers = {'Authorization': f'Bearer {access}'} #!пробел
response = requests.get(get_url('/api/users/'), headers=headers)
assert response.status_code == 200

timeout()
#Рефрешин токен(для объявления)
response = requests.post(get_url('/api/token/refresh'), data={'refresh': refresh})
result = response.json()

access = result['access']
print('Update token', access, end = f'\n{50*"#"}\n')
print('refresh', refresh, end=f'\n{50*"#"}\n')
timeout()
headers = {'Authorization': f'Bearer {access}'} #!пробел
response = requests.get(get_url('/api/users/'), headers=headers)
assert response.status_code == 200


