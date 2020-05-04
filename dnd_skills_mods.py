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

print(ability_mods)

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

print(bonus_list)
