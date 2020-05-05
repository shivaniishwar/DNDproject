import requests,json,random

#list all races
races = requests.get("https://www.dnd5eapi.co/api/races/")
race_result = json.loads(races.text)

race_list = {}
for row in race_result['results']:
    name = row['name']
    url = row['url']
    race_list.update({name:url})

#list all classes
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

raceclass = {}
raceclass['race_name'] = random_race
raceclass['race_url'] = "https://www.dnd5eapi.co"+race_list[random_race]
raceclass['class_name'] = random_class
raceclass['class_url'] = "https://www.dnd5eapi.co"+class_list[random_class]

#get details about race
race_details = requests.get("https://www.dnd5eapi.co"+race_list[random_race])
race_detail_result = json.loads(race_details.text)

#get subrace
if race_detail_result['subraces'] != []:
    subrace = random.choice(race_detail_result['subraces'])
    raceclass['subrace_name'] = subrace['name']
    raceclass['subrace_url'] = "https://www.dnd5eapi.co"+subrace['url']
else:
    pass

#get details about class
class_details = requests.get("https://www.dnd5eapi.co"+class_list[random_class])
class_detail_result = json.loads(class_details.text)

#get subclass
if class_detail_result['subclasses'] != []:
    subclass = random.choice(class_detail_result['subclasses'])
    raceclass['subclass_name'] = subclass['name']
    raceclass['subclass_url'] = "https://www.dnd5eapi.co"+subclass['url']
else:
    pass

#dump to file
with open("random_raceclass.json","w") as raceclass_file:
    json.dump(raceclass,raceclass_file)
