import requests
import json

cidade = input("Escreva sua cidade: ")

requisicao = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+cidade+'&appid=e5d9b5f5d36defff90206c1f4c8679f8')

tempo = json.loads(requisicao.text)

print('Condição do tempo: ', tempo['weather'][0]['main'])
print('Temperatura: ', float(tempo['main']['temp']) - 273.15)
