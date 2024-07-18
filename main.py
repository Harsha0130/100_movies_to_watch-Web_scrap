import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
web_data = response.text
# Write your code below this line 👇
soup = BeautifulSoup(web_data, "html.parser")

movie_title = soup.find_all(name="h3", class_="title")

movie_titles = [title.getText() for title in movie_title]

reversed_titles = movie_titles[::-1]

# The UnicodeEncodeError is likely due to special characters in
# some of the movie titles that cannot be encoded using the default encoding
with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in reversed_titles:
        file.write(f"{movie}\n")
