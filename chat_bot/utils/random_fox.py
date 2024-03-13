import requests

def fox():
    url = 'https://randomfox.ca/floof/' # API is Available (вставляем адрес разрешенного url)
    response = requests.get(url) # делаем запрос на этот url
    if response.status_code:
        data = response.json() # преобразуем данные из url в пайтоновский словарь
        return data.get('image') # возвращаем изображение по ключу из словаря
        #print(response.status_code) # проверяем номер запроса

if __name__ == "__main__":
    fox()