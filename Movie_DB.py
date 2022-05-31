import requests
import os

name = input("Please, enter the title of the movie: <<-- ")
year = '(' + input("Please, enter the year: <<-- ") + ')'

url_id = f"https://imdb-api.com/en/API/SearchMovie/k_yo59xtic/{name} {year}"


payload = {}
headers = {}

first_response = requests.request("GET", url_id, headers=headers, data=payload)

data = first_response.json()

movie_id = ''


for element in data['results']:
    if element['title'] == name and element['description'] == year:
        movie_id = element['id']

url = f"https://imdb-api.com/en/API/Title/k_yo59xtic/{movie_id}"

second_response = requests.request("GET", url, headers=headers, data=payload)

data = second_response.json()

title, director, year = data['title'], data['directors'], int(data['year'])

with open('query.txt', 'w') as file:
    file.write(f'''INSERT INTO Movies_seen VALUES ('{title}', '{director}', {year});''')

os.system('mysql -u root --password=Healter666Skelter --database=MOVIES < query.txt')

os.system('rm query.txt')


