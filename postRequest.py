import requests



url = 'http://192.168.1.65:3002/example.html'

response = requests.post(url, data={"Disciplina": "Arquitetura de Rede", "Professor": "Antonio Varela"})
print(response.status_code)
print(response.request.body)