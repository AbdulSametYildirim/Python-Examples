import sys
import requests
from bs4 import BeautifulSoup


r = requests.get("https://imdb.com/chart/top/")
if r.status_code == 200:
    print("you can extract data from website")
else:
    print("you can't extract data from website")

#print(r.content)
#print(r.text)
#print(r.encoding)

soup = BeautifulSoup(r.content,"html.parser")

for i in soup.find("tbody",{"class":"lister-list"}).find_all("tr"):
    film_name = i.find("td",{"class":"titleColumn"}).a.text
    get_year = i.find("span",{"class":"secondaryInfo"}).text.strip("()")
    get_star = i.find("td",{"class":"ratingColumn"}).strong.text
    print("-------------------------Film Info-------------------------")
    print(f"Film name: {film_name}\nFilm year: {get_year}\nFilm star: {get_star}\n")




































