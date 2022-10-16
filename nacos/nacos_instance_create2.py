import requests

params = {'ip': '10.53.179.14', 'port': '8002', 'serviceName': 'Python'}
url = "http://localhost:8848/nacos/v1/ns/instance"
res = requests.post(url, params=params)
print(res.text)