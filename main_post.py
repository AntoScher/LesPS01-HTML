import requests
from pprint import pprint
# URL для отправки POST-запроса
url = 'https://jsonplaceholder.typicode.com/posts'
# Данные для отправки
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}
# Выполнение POST-запроса с данными
response = requests.post(url, json=data)
# Печать статус-кода ответа
print('Status Code:', response.status_code)
# Печать содержимого ответа в формате JSON с использованием pprint
print('Response JSON:')
pprint(response.json())
