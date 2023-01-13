import requests
print('requests library version: ', requests.__version__)
print(requests.get('http://www.google.com/').text)