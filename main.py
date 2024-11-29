import requests
from bs4 import BeautifulSoup
import lxml

response=requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_txt=response.text
web=BeautifulSoup(web_txt,"lxml")
# print(web.title)
movie=web.find_all(name="h3",class_="title")
movie_name=[n.getText() for n in movie][::-1]
print(movie_name)
for n in movie_name:
    with open(file="movies.txt",mode="w",encoding="utf-8") as m:
        m.write(f"{n}\n")
