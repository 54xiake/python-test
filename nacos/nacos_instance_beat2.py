import requests
import json
import time

params = {}
url = "http://localhost:8848/nacos/v1/ns/instance/beat?serviceName=Python&beat=%7b%22ip%22%3a%22192.168.20.110%22%2c%22metadata%22%3a%7b%7d%2c%22port%22%3a8002%2c%22scheduled%22%3atrue%2c%22serviceName%22%3a%22Python%22%2c%22weight%22%3a1%7d"

# 模拟持续发送心跳
for num in range(0, 2000):
    res = requests.put(url, data=json.dumps(params))
    print(res.text)
    time.sleep(2)