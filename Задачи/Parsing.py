### https://dzen.ru/video/watch/615c436111c07c13075c370c

from bs4 import BeautifulSoup
from urllib.request import urlopen


url = [
    "https://habr.com/ru/post/580888/",
    "https://habr.com/ru/post/579100/",
]


file = open('article.txt', 'a', encoding='utf8')

for x in url:
    soup = BeautifulSoup(urlopen(x).read(), 'html.parser')

    s = soup.find('title').text
    file.write(s+'\n')
    p = soup.find_all('p')
    print(s)
    for j in p:
        print(j.text)
        file.write(j.text+'\n')

file.close()







# for x in url:


#     text = soup.find_all('p')
#     for j in text:
        


# class Parsing:
#     def __init__(self, url):
#         self.url = url
#         self.page = urlopen(self.url)
#         self.soup = BeautifulSoup(self.page.read(), 'html.parser')
        
        