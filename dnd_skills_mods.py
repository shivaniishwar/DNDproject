import requests,json,random

#read ability scores
sc = open("ability_scores.json")
scores = json.load(sc)

ability_mods = {}

for item in scores:
    number = scores[item]
    if number % 2 != 0:
        number = number-1
    mod = int((number - 10)/2)
    ability_mods.update({item:mod})

#get list of all skills
skills = requests.get("https://www.dnd5eapi.co/api/skills")
skills_result = json.loads(skills.text)

skill_list = {}

for item in skills_result['results']:
    name = item['name']
    url = item['url']
    skill_list.update({name:url})

bonus_list = {}

#figure out which skills get which bonuses
for skill in skill_list:
    info = requests.get("https://www.dnd5eapi.co"+skill_list[skill])
    info_result = json.loads(info.text)
    corresponding_score = info_result['ability_score']['name'].lower()
    score_bonus = ability_mods[corresponding_score]
    bonus_list.update({skill:score_bonus})

#add proficiencies
pr = open("random_proficiencies.json")
prof = json.load(pr)

proficiency_bonus = 2

for item in prof:
    name = item['name'][7:]
    for item in bonus_list:
        if item == name:
            bonus_list[item] = bonus_list[item] + proficiency_bonus

rc = open("random_raceclass.json")
raceclass = json.load(rc)

x = requests.get(raceclass['race_url'])
x_result = json.loads(x.text)
speed = x_result['speed']

save = requests.get(raceclass['class_url'])
save_result = json.loads(save.text)
saves = []
for item in save_result['saving_throws']:
    name = item['name'].lower()
    saves.append(name)
hp_base = save_result['hit_die']

saving_throws = {}
for item in ability_mods:
    saving_throws[item] = ability_mods[item]

for item in saving_throws:
    if item in saves:
        saving_throws[item] = saving_throws[item] + proficiency_bonus

armor_class = 10+ability_mods['dex']
initiative_bonus = ability_mods['dex']
passive_perception = 10+ability_mods['wis']
hit_points = hp_base+ability_mods['con']

other_scores = {
                "Armor Class":armor_class,
                "Initiative":initiative_bonus,
                "Passive Perception":passive_perception,
                "Hit Points": hit_points,
                "Hit Dice": "1d"+str(hp_base),
                "Speed": speed,
                "Proficiency Bonus": proficiency_bonus
                }

with open("ability_mods.json","w") as mods_file:
    json.dump(ability_mods,mods_file)

with open("saving_throws.json","w") as st_file:
    json.dump(saving_throws,st_file)

with open("skills.json","w") as skill_file:
    json.dump(bonus_list,skill_file)

with open("other_scores.json","w") as other_file:
    json.dump(other_scores,other_file)
