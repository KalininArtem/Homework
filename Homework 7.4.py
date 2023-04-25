import requests
import json

from requests.exceptions import RequestException

def get_heroes_data():
    try:
        text = requests.get("https://akabab.github.io/superhero-api/api/all.json")
    except RequestException:
        print("Ошибка при доступе к сайту")
    else:
        return text.text


def find_heroes_stats(heroes, database: str):
    superheroes = {}
    for hero in json.loads(database):
        if hero["name"] in heroes:
            superheroes.update([(hero["name"], hero["powerstats"]["intelligence"])])
    return superheroes


def find_smartest_hero(heroes):
    max_intelligence = max(list(heroes.values()))
    for hero in heroes:
        if heroes[hero] == max_intelligence:
            print(f"Smartest hero: {hero}, intelligence: {heroes[hero]}")
            break

names = ['Hulk', 'Captain America', 'Thanos']
heroes_data = get_heroes_data()
heroes_p = find_heroes_stats(names, heroes_data)
find_smartest_hero(heroes_p)






