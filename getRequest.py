import requests



url = 'http://127.0.0.1:3002/example.html'

response = requests.get(url)
print(response.text)
