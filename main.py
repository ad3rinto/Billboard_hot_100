import requests
from bs4 import BeautifulSoup

year_of_travel = input("What year will you like to travel to ? YYY-MM-DD format please: ")
# print(year_of_travel)

URL = f"https://www.billboard.com/charts/hot-100/{year_of_travel}/"

web_data = requests.get(URL)
content = web_data.text

soup = BeautifulSoup(content, "html.parser")
# print(soup.prettify())

title = soup.findAll("h3", class_="c-title")
for i in title:
    print(i.text)
