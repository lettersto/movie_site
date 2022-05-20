import requests
import json

with open('movies.json', encoding='UTF8') as a:
    dict1 = json.load(a)
movie_pk_list = []
for movie in dict1:
    movie_pk_list.append(movie['pk'])
# print(movie_pk_list)

API_KEY = '5a0120685758c69e340f0976820a2dbc'

actor_list = []
director_list = []

for movie_pk in movie_pk_list:
    URL = f'https://api.themoviedb.org/3/movie/{movie_pk}/credits?api_key={API_KEY}'
    res = requests.get(URL).json()
    cast_set = res.get('cast')
    crew_set = res.get('crew')
    castname_set = []
    for i in range(len(cast_set)):
        if cast_set[i]['cast_id'] < 5:
            castname_set.append(cast_set[i]['name'])
    actor_dict = {
        "model": "movies.actor",
        "pk": movie_pk,
        "fields": {
        "name": castname_set,
        }
    }
    actor_list.append(actor_dict)
    crewname_set = []
    for j in range(len(crew_set)):
        if crew_set[j]['department'] == 'Directing':
            crewname_set.append(crew_set[j]['name'])
    director_dict = {
        "model": "movies.director",
        "pk": movie_pk,
        "fields": {
        "name": crewname_set,
        }
    }
    director_list.append(director_dict)

# print(actor_list)
# print(director_list)


with open('actor.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps(actor_list, ensure_ascii=False, indent=4))

with open('director.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps(director_list, ensure_ascii=False, indent=4))