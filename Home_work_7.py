
import requests

heroes_data = requests.get('https://akabab.github.io/superhero-api/api/all.json').json()
heroes = list(filter(lambda hero: hero['name'] in ['Hulk', 'Captain America', 'Thanos'], heroes_data))
super_man = []
for power_stats in heroes:
                super_man.append({
                    'name': power_stats['name'],
                    'intelligence': power_stats['powerstats']['intelligence'],
                })

intelligence_super_hero = 0
name = ''
for intelligence_hero in super_man:
     if intelligence_super_hero < int(intelligence_hero['intelligence']):
        intelligence_super_hero = int(intelligence_hero['intelligence'])
        name = intelligence_hero['name']

print(f"Самый интелектуальный {name}, интелект: {intelligence_super_hero}")
