import requests
 
response = requests.get('https://zenquotes.io/api/random')
data = response.json()
 
divider = '-' * 50
 
print(divider)
print(data[0]['q'])
print('—', data[0]['a'])
print(divider)
