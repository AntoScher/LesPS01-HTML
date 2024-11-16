import requests
from pprint import pprint
# URL для запроса к API JSONPlaceholder с параметром userId=1
url = 'https://jsonplaceholder.typicode.com/posts'
params = {
    'userId': 1
}
# Выполнение GET-запроса с параметрами
response = requests.get(url, params=params)
# Проверка статуса ответа
print('Status Code:', response.status_code)
# Печать полученных записей в формате JSON с использованием pprint
print('Response JSON:')
pprint(response.json())
