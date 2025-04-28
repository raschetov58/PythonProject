import requests
import json


response = requests.post('http://users.bugred.ru/tasks/rest/doregister', json={
    "email": "odaisu@yandex.ru",
    "name": "Саша",
    "password": "1"
})
'''response_put = requests.put('http://users.bugred.ru/tasks/rest/addavatar', json={
    "email": "odaisu@yandex.ru",
    "name": "Саша",
    "password": "1"
})'''



'''response = requests.get('https://belarusbank.by/api/kursExchange?city=Брест')'''