import requests

data = {
    'count': '1'
}
responce = requests.post('http://localhost:8000/api/v1/ping/', json=data)
print(responce.text)
