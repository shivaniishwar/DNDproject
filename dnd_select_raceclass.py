import requests,json, random

#list races
races = requests.get("https://www.dnd5eapi.co/api/races/")
race_result = json.loads(races.text)

race_list = {}
for row in race_result['results']:
    name = row['name']
    url = row['url']
    race_list.update({name:url})

#list classes
classes = requests.get("https://www.dnd5eapi.co/api/classes/")
class_result = json.loads(classes.text)

class_list = {}
for row in class_result['results']:
    name = row['name']
    url = row['url']
    class_list.update({name:url})

#choose a race and class at random
random_race = random.choice(list(race_list))
random_class = random.choice(list(class_list))
print(random_race, random_class)

#get details about race
race_details = requests.get("https://www.dnd5eapi.co"+race_list[random_race])
race_detail_result = json.loads(race_details.text)
print(race_detail_result['subraces'])

#get details about class
class_details = requests.get("https://www.dnd5eapi.co"+class_list[random_class])
class_detail_result = json.loads(class_details.text)
print(class_detail_result['subclasses'])
