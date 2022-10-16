import requests

params = {'serviceName': 'Python', 'protectThreshold': '0'}
url = "http://localhost:8848/nacos/v1/ns/service"

res = requests.post(url, params=params)
print(res.text)