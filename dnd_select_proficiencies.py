import requests,json,random

#read in random race/class
rc = open("random_raceclass.json")
raceclass = json.load(rc)

#initialize list of proficiencies
proficiencies = []

#find race proficiencies
chosen_race = requests.get(raceclass['race_url'])
race_result = json.loads(chosen_race.text)

for item in race_result['starting_proficiencies']:
    proficiencies.append(item)

#find class proficiencies
chosen_class = requests.get(raceclass['class_url'])
class_result = json.loads(chosen_class.text)

choice_number = class_result['proficiency_choices'][0]['choose']
class_profs = random.sample(class_result['proficiency_choices'][0]['from'],choice_number)

#gather all proficiencies
for item in class_profs:
    proficiencies.append(item)

#dump to file
with open ("random_proficiencies.json","w") as proficiencies_file:
    json.dump(proficiencies,proficiencies_file)
