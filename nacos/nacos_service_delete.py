import requests

params = {}
url = "http:/localhost:8848/nacos/v1/ns/service?serviceName=Python"
res = requests.delete(url, params=params)
print(res.text)