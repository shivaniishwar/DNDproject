import requests,json,random

#get race + class information
rc = open("random_raceclass.json")
raceclass = json.load(rc)

race_get = requests.get(raceclass['race_url'])
race_info = json.loads(race_get.text)
try:
    subrace_get = requests.get(raceclass['subrace_url'])
    subrace_info = json.loads(subrace_get.text)
except:
    pass
class_get = requests.get(raceclass['class_url'])
class_info = json.loads(class_get.text)

#get languages from race/subrace
languages = []
try:
    for item in race_info['languages']:
        languages.append(item['name'])
except:
    pass
try:
    lang_options = random.sample(race_info['language_options']['from'],race_info['language_options']['choose'])
    for item in lang_options:
        languages.append(item['name'])
except:
    pass

try:
    for item in subrace_info['languages']:
        languages.append(item['name'])
except:
    pass
try:
    lang_2 = random.sample(subrace_info['language_options']['from'],subrace_info['language_options']['choose'])
    for item in lang_2:
        languages.append(item['name'])
except:
    pass

languages = list(dict.fromkeys(languages))

#get traits from race/subrace
traits_initial = {}
traits = {}

try:
    for item in race_info['traits']:
        name = item['name']
        url = item['url']
        traits_initial.update({name:url})
except:
    pass
try:
    add_traits = random.sample(race_info['trait_options']['from'],race_info['trait_options']['choose'])
    for item in add_traits:
        name = item['name']
        url = item['url']
        traits_initial.update({name:url})
except:
    pass
try:
    for item in subrace_info['racial_traits']:
        name = item['name']
        url = item['url']
        traits_initial.update({name:url})
except:
    pass
try:
    add_traits_2 = random.sample(subrace_info['racial_trait_options']['from'],
                   subrace_info['racial_trait_options']['choose'])
    for item in add_traits_2:
        name = item['name']
        url = item['url']
        traits_initial.update({name:url})
except:
    pass

for item in traits_initial:
    trait_get = requests.get("https://dnd5eapi.co"+traits_initial[item])
    trait_info = json.loads(trait_get.text)
    name = item
    desc = trait_info['desc']
    traits.update({name:desc})

#get equipment from class
req_url = class_info['starting_equipment']['url']
equip_get = requests.get("https://dnd5eapi.co"+req_url)
equip_info = json.loads(equip_get.text)

equipment = {}

for item in equip_info['starting_equipment']:
    eq_item = item['item']['name']
    number = item['quantity']
    equipment.update({eq_item:number})

number_of_choices = equip_info['choices_to_make']

for i in range(1,number_of_choices+1):
    chooser = equip_info['choice_'+str(i)]
    if len(chooser) == 1:
        choose_num = chooser[0]['choose']
        choose_from = chooser[0]['from']
        equip_choice = random.sample(choose_from,choose_num)
        eq_item = equip_choice[0]['item']['name']
        number = equip_choice[0]['quantity']
        equipment.update({eq_item:number})
    else:
        choosing = random.choice(chooser)
        choose_num = choosing['choose']
        choose_from = choosing['from']
        equip_choice = random.sample(choose_from,choose_num)
        eq_item = equip_choice[0]['item']['name']
        number = equip_choice[0]['quantity']
        equipment.update({eq_item:number})

#export everything to files!

with open("languages.json","w") as lang_file:
    json.dump(languages,lang_file)

with open("traits.json","w") as trait_file:
    json.dump(traits,trait_file)

with open("equipment.json","w") as equip_file:
    json.dump(equipment,equip_file)
