import requests

response = requests.get('https://zenquotes.io/api/random')
data = response.json()

print(data[0]['q'])
print('—', data[0]['a'])
