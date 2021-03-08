# Utilisation de la librairie PySimpleAutomata pour générer des automates à partir de fichiers json
# Doc: https://pysimpleautomata.readthedocs.io/en/latest/automata_IO.html#PySimpleAutomata.automata_IO.dfa_to_dot
#

from PySimpleAutomata import DFA, automata_IO
from pathlib import Path
import os

# Récupération des fichiers .json à traiter
path = Path('..\\Results\\')
input_json_files = (
    entry for entry in path.iterdir() if entry.is_file())

for filename in input_json_files:
    with open(os.path.join(os.getcwd(), filename), 'r') as f:  # ouvrir en mode lecture
        print(filename)
        extension = filename.name.split('.')  # nom du fichier
        if extension[1] == 'json':
            name = extension[0]
            print(name)

            # dfa_example = automata_IO.dfa_dot_importer('./input.dot')
            # Importer le fichier json
            dfa_example = automata_IO.dfa_json_importer(filename)

            # DFA.dfa_completion(dfa_example)
            # new_dfa = DFA.dfa_minimization(dfa_example)

            # automata_IO.dfa_to_json(new_dfa, 'output-name', './output')
            # Exporter le graphe de json vers dot et graphe format svg
            automata_IO.dfa_to_dot(
                dfa_example, name, os.path.join(os.getcwd(), path))
