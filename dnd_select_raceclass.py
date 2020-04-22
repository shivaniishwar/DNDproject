import requests,json, random

#list races
races = requests.get("https://www.dnd5eapi.co/api/races/")
race_result = json.loads(races.text)

race_list = {}
for row in race_result['results']:
    name = row['name']
    url = row['url']
    race_list.update({name:url})

random_race = random.choice(list(race_list))
print(random_race)

#list classes
classes = requests.get("https://www.dnd5eapi.co/api/classes/")
class_result = json.loads(classes.text)

class_list = {}
for row in class_result['results']:
    name = row['name']
    url = row['url']
    class_list.update({name:url})

random_class = random.choice(list(class_list))
print(random_class)
