import requests
import json

API_KEY = '5a0120685758c69e340f0976820a2dbc'
genre_list = []
URL = f'https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language=ko'
res = requests.get(URL).json()
genre_set = res.get('genres')

for genre in genre_set:
    genre_dict = {
        "model": "movies.genre",
        "pk": genre.get("id"),
        "fields": {
            "name": genre.get("name"),
        }
    }
    genre_list.append(genre_dict)

# print(genre_list)
with open('genres.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps(genre_list, ensure_ascii=False, indent=4))