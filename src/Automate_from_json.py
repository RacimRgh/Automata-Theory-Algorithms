# # Utilisation de la librairie PySimpleAutomata pour générer des automates à partir de fichiers json
# # Doc: https://pysimpleautomata.readthedocs.io/en/latest/automata_IO.html#PySimpleAutomata.automata_IO.dfa_to_dot
# #

# # Migration vers graphviz de pypi
# # https://graphviz.readthedocs.io/en/stable/

# from PySimpleAutomata import DFA, automata_IO
from pathlib import Path
import os

# # Récupération des fichiers .json à traiter
# path = Path('..\\Results\\')
# input_json_files = (
#     entry for entry in path.iterdir() if entry.is_file())

# for filename in input_json_files:
#     with open(os.path.join(os.getcwd(), filename), 'r') as f:  # ouvrir en mode lecture
#         print(filename)
#         extension = filename.name.split('.')  # nom du fichier
#         if extension[1] == 'json':
#             name = extension[0]
#             print(name)

#             # dfa_example = automata_IO.dfa_dot_importer('./input.dot')
#             # Importer le fichier json
#             dfa_example = automata_IO.dfa_json_importer(filename)

#             # DFA.dfa_completion(dfa_example)
#             # new_dfa = DFA.dfa_minimization(dfa_example)

#             # automata_IO.dfa_to_json(new_dfa, 'output-name', './output')
#             # Exporter le graphe de json vers dot et graphe format svg
#             automata_IO.dfa_to_dot(
#                 dfa_example, name, os.path.join(os.getcwd(), path))

from graphviz import Digraph
import json

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
            automate = Digraph('finite_state_machine', directory=os.path.join(
                os.getcwd(), path), filename=name, format='png')
            graph = json.load(f)
            automate.attr('node', shape='doublecircle')
            for final_state in graph['accepting_states']:
                automate.node(final_state)
            automate.attr('node', shape='circle')
            for state in graph['transitions']:
                automate.edge(state[0], state[2], label=state[1])
            automate.view()


# f.attr(rankdir='LR', size='8,5')

# f.attr('node', shape='doublecircle')
# f.node('LR_0')
# f.node('LR_3')
# f.node('LR_4')
# f.node('LR_8')

# f.attr('node', shape='circle')
# f.edge('LR_0', 'LR_2', label='SS(B)')
# f.edge('LR_0', 'LR_1', label='SS(S)')
# f.edge('LR_1', 'LR_3', label='S($end)')
# f.edge('LR_2', 'LR_6', label='SS(b)')
# f.edge('LR_2', 'LR_5', label='SS(a)')
# f.edge('LR_2', 'LR_4', label='S(A)')
# f.edge('LR_5', 'LR_7', label='S(b)')
# f.edge('LR_5', 'LR_5', label='S(a)')
# f.edge('LR_6', 'LR_6', label='S(b)')
# f.edge('LR_6', 'LR_5', label='S(a)')
# f.edge('LR_7', 'LR_8', label='S(b)')
# f.edge('LR_7', 'LR_5', label='S(a)')
# f.edge('LR_8', 'LR_6', label='S(b)')
# f.edge('LR_8', 'LR_5', label='S(a)')

# f.view()
