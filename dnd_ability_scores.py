import requests,json,random

#list abilities
abilities = requests.get("https://www.dnd5eapi.co/api/ability-scores/")
abilities_result = json.loads(abilities.text)

ability_names = []
for row in abilities_result['results']:
    name = row['index']
    ability_names.append(name)

#assign random values to the scores
#this is done by "rolling" four 6-sided dice, then dropping the lowest roll, then adding them all together
scores = []
for i in range(6):
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    roll3 = random.randint(1,6)
    roll4 = random.randint(1,6)
    nums = [roll1,roll2,roll3,roll4]
    lowest = min(nums)
    score = roll1 + roll2 + roll3 + roll4 - lowest
    scores.append(score)

random.shuffle(scores)

ability_scores = {}

for i in range(6):
    name = ability_names[i]
    score = scores[i]
    ability_scores.update({name:score})

#add in bonuses
rc = open("random_raceclass.json")
raceclass = json.load(rc)

bonus_get = requests.get(raceclass['race_url'])
bonuses_1 = json.loads(bonus_get.text)

for item in bonuses_1['ability_bonuses']:
    name = item['name'].lower()
    add = item['bonus']
    for score in ability_scores:
        if score == name:
            ability_scores[score] = ability_scores[score] + add

try:
    bonus_sub = requests.get(raceclass['subrace_url'])
    bonuses_2 = json.loads(bonus_sub.text)

    for item in bonuses_2['ability_bonuses']:
        name = item['name'].lower()
        add = item['bonus']
        for score in ability_scores:
            if score == name:
                ability_scores[score] = ability_scores[score] + add
except:
    pass

with open ("ability_scores.json","w") as score_file:
    json.dump(ability_scores,score_file)
