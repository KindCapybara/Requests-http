import requests


def get_hero(name):
    uri = 'https://akabab.github.io/superhero-api/api/all.json'
    all_hero = requests.get(uri).json()
    hero_intelligence = {}
    for i in all_hero:
        if i['name'] in name:
            hero_intelligence[i['name']] = i['powerstats']['intelligence']
    print(max(hero_intelligence))


get_hero(['Hulk', 'Captain America', 'Thanos'])
