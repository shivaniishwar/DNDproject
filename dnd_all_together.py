import json,random

#okay, all the data exists! time to put it all together!

#open our many json files
r_c = open("random_raceclass.json")
raceclass = json.load(r_c)
a_s = open("ability_scores.json")
ability_scores = json.load(a_s)
a_m = open("ability_mods.json")
ability_mods = json.load(a_m)
s_t = open("saving_throws.json")
saving_throws = json.load(s_t)
sk = open("skills.json")
skills = json.load(sk)
o_s = open("other_scores.json")
scores = json.load(o_s)
s_i = open("spellcasting_info.json")
spells = json.load(s_i)
l = open("languages.json")
lang = json.load(l)
t = open("traits.json")
traits = json.load(t)
e = open("equipment.json")
equipment = json.load(e)

#create output dictionary
character = {}

#let user choose a name
char_name = input("NAME YOUR CHARACTER: ")
character.update({"NAME":char_name})

#build the rest of our character info
race_string = raceclass['race_name']
if "subrace_name" in raceclass:
    race_string = race_string+" ("+raceclass['subrace_name']+")"
character.update({"RACE":race_string})

class_string = raceclass['class_name']
if "subclass_name" in raceclass:
    class_string = class_string+" ("+raceclass['subclass_name']+")"
character.update({"CLASS":class_string})

align_gne = ['Good','Neutral','Evil']
align_lnc = ['Lawful','Neutral','Chaotic']
align_c1 = random.choice(align_lnc)
align_c2 = random.choice(align_gne)
alignment = align_c1+' '+align_c2
if alignment == "Neutral Neutral":
    alignment = "True Neutral"
character.update({"ALIGNMENT":alignment})

character.update({"LEVEL":1})

speed_string = str(scores['Speed'])+" feet per round"
character.update({"SPEED":speed_string})

character.update({"ARMOR CLASS":scores['Armor Class']})

if scores['Initiative'] <= 0:
    init_string = str(scores['Initiative'])
else:
    init_string = "+"+str(scores['Initiative'])
character.update({"INITIATIVE BONUS":init_string})

if scores['Proficiency Bonus'] <= 0:
    prof_string = str(scores['Proficiency Bonus'])
else:
    prof_string = "+"+str(scores['Proficiency Bonus'])
character.update({"PROFICIENCY BONUS":prof_string})
character.update({"HIT POINTS":scores['Hit Points']})
character.update({"HIT DICE":scores['Hit Dice']})

abilities = {}

cha = {"Score":ability_scores['cha'],"Modifier":ability_mods['cha'],"Saving Throw":saving_throws['cha']}
con = {"Score":ability_scores['con'],"Modifier":ability_mods['con'],"Saving Throw":saving_throws['con']}
dex = {"Score":ability_scores['dex'],"Modifier":ability_mods['dex'],"Saving Throw":saving_throws['dex']}
int = {"Score":ability_scores['int'],"Modifier":ability_mods['int'],"Saving Throw":saving_throws['int']}
str = {"Score":ability_scores['str'],"Modifier":ability_mods['str'],"Saving Throw":saving_throws['str']}
wis = {"Score":ability_scores['wis'],"Modifier":ability_mods['wis'],"Saving Throw":saving_throws['wis']}

abilities.update({"Charisma":cha})
abilities.update({"Constitution":con})
abilities.update({"Dexterity":dex})
abilities.update({"Intelligence":int})
abilities.update({"Strength":str})
abilities.update({"Wisdom":wis})

character.update({"ABILITIES":abilities})

character.update({"SKILL BONUSES":skills})

character.update({"LANGUAGES":lang})

character.update({"TRAITS":traits})

character.update({"SPELLCASTING":spells})

character.update({"EQUIPMENT":equipment})

#write to a new json file
with open("character.json","w") as char_file:
    json.dump(character,char_file)
