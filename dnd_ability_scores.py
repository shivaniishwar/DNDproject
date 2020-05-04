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
