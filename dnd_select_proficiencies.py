import requests,json,random

#read random race/class
rc = open("random_raceclass.json")
raceclass = json.load(rc)

print(raceclass)

#initialize list of proficiencies
proficiencies = []

#race proficiencies
chosen_race = requests.get(raceclass['race_url'])
race_result = json.loads(chosen_race.text)

for item in race_result['starting_proficiencies']:
    proficiencies.append(item)

#class proficiencies
chosen_class = requests.get(raceclass['class_url'])
class_result = json.loads(chosen_class.text)

choice_number = class_result['proficiency_choices'][0]['choose']
class_profs = random.sample(class_result['proficiency_choices'][0]['from'],choice_number)

for item in class_profs:
    proficiencies.append(item)

for item in proficiencies:
    print(item['name'])
