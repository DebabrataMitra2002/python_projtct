import pandas as pd
import requests 
from bs4 import BeautifulSoup as bs

url = "https://www.yogsutra.com/bangladeshi-computer-magazines.html"

page = requests.get(url)

# print(page.content)
soup = bs(page.content,'html.parser')
# print(soup)
print(soup.find("ul",class_="").text)
for link in soup.find_all('a',rel_="nofollow"):
   print(link.get('href'))