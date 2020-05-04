import requests,json,random

#get class information
rc = open("random_raceclass.json")
raceclass = json.load(rc)

char_class = raceclass['class_name']

spell_check = requests.get('https://www.dnd5eapi.co/api/spellcasting')
sc_json = json.loads(spell_check.text)

for item in sc_json['results']:
    if char_class in item['class']:
        spell_url = item['url']

if "spell_url" in locals():
    casting = requests.get('https://www.dnd5eapi.co'+spell_url)
    casting_json = json.loads(casting.text)
    if casting_json['level'] == 1:
        spellcasting = True
    else:
        spellcasting = False
else:
    spellcasting = False

#get spellcasting modifiers
if spellcasting == True:
    casting = requests.get('https://www.dnd5eapi.co'+spell_url)
    casting_json = json.loads(casting.text)
    ability = casting_json['spellcasting_ability']['name'].lower()
    mods = open("ability_mods.json")
    a_mods = json.load(mods)
    p = open("other_scores.json")
    prof = json.load(p)
    spell_attack = a_mods[ability] + prof['Proficiency Bonus']
    spell_dc = 8 + a_mods[ability] + prof['Proficiency Bonus']
    spell_mods = {'Attack': spell_attack,'DC': spell_dc}
    with open("spell_mods.json","w") as mod_file:
        json.dump(spell_mods,mod_file)

#number of spells: this is NOT included in the API!
#... so i manually transcribed it from the long text segments ^^"
if char_class == "Bard":
    cantrips = 2
    spells = 4
    spell_slots = 2
    spell_refresh = "level up"
if char_class == "Cleric":
    cantrips = 3
    spells = a_mods['wis'] + 1
    if spells < 1:
        spells = 1
    spell_slots = 2
    spell_refresh = "long rest"
if char_class == "Druid":
    cantrips = 2
    spells = a_mods['wis'] + 1
    if spells < 1:
        spells = 1
    spell_slots = 2
    spell_refresh = "long rest"
if char_class == "Sorcerer":
    cantrips = 4
    spells = 2
    spell_slots = 2
    spell_refresh = "level up"
if char_class == "Warlock":
    cantrips = 2
    spells = 2
    spell_slots = 1
    spell_refresh = "level up"
if char_class == "Wizard":
    cantrips = 3
    spells = a_mods['int'] + 1
    if spells < 1:
        spells = 1
    spell_slots = 2
    spell_refresh =  "long rest"

#get full spell lists!
if spellcasting == True:
    cantrip_list = []
    spell_list = []

    all_spells = requests.get('https://www.dnd5eapi.co/api/spells')
    full_spell_list = json.loads(all_spells.text)
    for item in full_spell_list['results']:
        this_spell = requests.get('https://www.dnd5eapi.co'+item['url'])
        spell_info = json.loads(this_spell.text)
        lvl = spell_info['level']
        name = spell_info['name']
        for x in spell_info['classes']:
            if x['name'] == char_class:
                if lvl == 0:
                    cantrip_list.append(name)
                if lvl == 1:
                    spell_list.append(name)

    #final spell lists
    cantrips_known = random.sample(cantrip_list,cantrips)
    spells_known = random.sample(spell_list,spells)

    spell_info = {
                  "Cantrips":cantrips_known,
                  "Spells":spells_known,
                  "Spell Slots":spell_slots,
                  "New Spells":"every "+spell_refresh,
                  "Spell Attack Bonus":spell_attack,
                  "Spell DC":spell_dc
                 }
    with open("spellcasting_info.json","w") as spellfile:
        json.dump(spell_info,spellfile)
