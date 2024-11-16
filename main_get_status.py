import requests
from pprint import pprint
# URL для запроса к API GitHub с параметром поиска репозиториев с кодом HTML
url = 'https://api.github.com/search/repositories'
# Параметры запроса
params = {
    'q': 'html '
}
# Выполнение GET-запроса
response = requests.get(url, params=params)

# Печать статус-кода ответа
print('Status Code:', response.status_code)

# Печать содержимого ответа в формате JSON с использованием pprint
print('Response JSON:')
pprint(response.json())
