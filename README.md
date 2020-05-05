# DNDproject
a project using Python programming to create a 5th Edition Dungeons &amp; Dragons character generator.

This project consists of 7 Python scripts and ultimately results in one JSON file containing all the information for a D&D character. There are two ways of executing this process.

1) Use the shell script! "dnd_run_everything.sh" is a shell script that works in Terminal (command line for Mac) and will run all the Python scripts in sequence, delete extra JSON files, and open the final character JSON file in Atom.

2) If that shell script doesn't work for your OS, you can still run the process manually. Here are the steps in order:
  a. Run "dnd_select_raceclass.py"
  b. Run "dnd_select_proficiencies.py"
  c. Run "dnd_ability_scores.py"
  d. Run "dnd_skills_mods.py"
  e. Run "dnd_spells.py"
  f. Run "dnd_extra_stuff.py"
  g. Run "dnd_all_together.py"
 After all these steps, the final character will be in "character.json"; all other JSON files can be deleted at this point without losing any information.
