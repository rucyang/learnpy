import requests
import json


url = 'https://www.zhihu.com/search?type=content&q=python+pandas'
resp = requests.get(url)
print(resp)

data = json.loads(resp.text)
print(data.keys())
