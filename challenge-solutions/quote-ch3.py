import requests
 
response = requests.get('https://zenquotes.io/api/quotes')
data = response.json()
 
divider = '-' * 50
 
for i in range(3):
    print(divider)
    print(data[i]['q'])
    print('—', data[i]['a'])
 
print(divider)
