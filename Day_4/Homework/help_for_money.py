import requests
import json
from pprint import pprint

url = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(url)
# Variant 1
# data_dict = json.loads(response.text)
# print(type(data_dict))

# Variant 2
data_dict = response.json()
print(type(data_dict))


pprint(data_dict)
print(data_dict['Valute']['EUR']['Value'])
print(data_dict['Valute']['USD']['Value'])


