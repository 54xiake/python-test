import requests

params = {}
url = "http://localhost:8848/nacos/v1/ns/instance?serviceName=Python&ip=192.168.1.110&port=8001"

res = requests.delete(url, params=params)
print(res.text)