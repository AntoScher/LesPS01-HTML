import requests
from bs4 import BeautifulSoup

url="http://quotes.toscrape.com/"
response=requests.get(url)

html=response.text
soup=BeautifulSoup(html, "html.parser")
text=soup.find_all("span", class_="text")
print(text)
author=soup.find_all("small", class_="author")
print(author)
for i in range(len(text)):
    print(f"цитата- {i+1}")
    print(text[i].text)
    
    print(f"автор цитаты- {i+1}\n")
    print(author[i].text)




#links=soup.find_all("a")for link in links:#print(link) print(link.get("href"))

