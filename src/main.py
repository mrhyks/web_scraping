import requests
from bs4 import BeautifulSoup

res = requests.get("https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(res.text, 'html.parser')

top_items = []

for elem in soup.select('div.thumbnail'):
    top_items.append({
        "name": elem.select('h4 > a')[0].text.strip(),
        "description": elem.select('p.description')[0].text.strip()
    })
    

print(top_items)

image_items = []
for image in soup.select('img'):
    image_items.append({"src": image.get('src'), "alt": image.get('alt')})
    
print(image_items)

links = []
for a_tag in soup.select('a'):
    href = a_tag.get('href')
    text = a_tag.text
    
    if isinstance(href, list):
        href = ' '.join(href)
        
    links.append({'href': href.strip() if href is not None else '', 'text': text if text is not None else ''})
    
print(links)
