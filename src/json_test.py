import requests
from bs4 import BeautifulSoup
import json


file_name = 'data.json'

res = requests.get('https://codedamn.com')
with open(file_name, 'w') as file:
    json.dump(res.text, file)