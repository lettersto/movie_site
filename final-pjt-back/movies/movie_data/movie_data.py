import requests
import json

API_KEY = '5a0120685758c69e340f0976820a2dbc'
movie_list = []

for page in range(1, 2):
    URL = f'https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=ko-kr&page={page}'
    res = requests.get(URL).json()
    movie_set = res.get('results')

    for movie in movie_set:
        movie_dict = {
            "model": "movies.movie",
            "pk": movie.get("id"),
            "fields": {
                "title": movie.get('title'),
                "overview": movie.get('overview'),
                "poster_url": movie.get('poster_path'),
                "release_date": movie.get('release_date'),
                "genres": movie.get('genre_ids'),
                "actor": [movie.get("id")],
                "director": [movie.get("id")],
            }
        }
        movie_list.append(movie_dict)

# print(movie_list)
with open('movies3.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps(movie_list, ensure_ascii=False, indent=4))