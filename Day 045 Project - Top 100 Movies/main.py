import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
hundred_movies_webpage = response.text

soup = BeautifulSoup(hundred_movies_webpage, "html.parser")
articles = soup.find_all(name="h3", class_="title")
movies_names = []

for movies_name in articles:
    movie_name = movies_name.getText()
    movies_names.append(movie_name)

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movies in reversed(movies_names):
        file.write(movies + "\n")
