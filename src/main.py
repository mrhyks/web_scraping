import requests

res = requests.get('https://codedamn.com')


txt = res.text
status = res.status_code

print(txt, status)