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

#get equipment from class
