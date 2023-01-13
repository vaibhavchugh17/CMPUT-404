import requests

print('Requests library version: ', requests.__version__)
print()
print(requests.get('http://www.google.com/').text)
print()
print(requests.get('https://raw.githubusercontent.com/vaibhavchugh17/CMPUT-404/main/Lab%201/script.py').text)