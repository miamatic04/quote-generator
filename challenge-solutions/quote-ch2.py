import requests
 
response = requests.get('https://zenquotes.io/api/random')
data = response.json()
 
quote = data[0]['q']
author = data[0]['a']
 
with open('quote.txt', 'w') as f:
    f.write(quote + '\n')
    f.write('- ' + author + '\n')
 
print('Quote saved to quote.txt!')
