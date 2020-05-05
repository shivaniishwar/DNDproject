#!/bin/bash

# purpose of this script:
# run python scripts
# delete extra json files
# open character.json

# run python scripts
python3 dnd_select_raceclass.py
python3 dnd_select_proficiencies.py
python3 dnd_ability_scores.py
python3 dnd_skills_mods.py
python3 dnd_spells.py
python3 dnd_extra_stuff.py
python3 dnd_all_together.py

# delete extra json files
rm ability_mods.json
rm ability_scores.json
rm equipment.json
rm languages.json
rm other_scores.json
rm random_proficiencies.json
rm random_raceclass.json
rm saving_throws.json
rm skills.json
rm spellcasting_info.json
rm traits.json

# open character.json
open -a Atom character.json
# replace "Atom" with your favorite text editor!
