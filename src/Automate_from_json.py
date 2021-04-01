# # Migration vers graphviz de pypi
# # https://graphviz.readthedocs.io/en/stable/
from graphviz import Digraph
import json
from pathlib import Path
import os


def generate_automate():
    # Récupération des fichiers .json à traiter
    path = Path('..\\Results\\')
    input_json_files = (
        entry for entry in path.iterdir() if entry.is_file())

    for filename in input_json_files:
        with open(os.path.join(os.getcwd(), filename), 'r') as f:  # ouvrir en mode lecture
            print(filename)
            extension = filename.name.split('.')  # nom du fichier
            if len(extension) > 1 and extension[1] == 'json':
                name = extension[0]
                print(name)
                automate = Digraph('finite_state_machine', directory=os.path.join(
                    os.getcwd(), path), filename=name, format='png')
                graph = json.load(f)

                automate.attr('node', shape='egg')
                automate.node(graph['initial_state'])

                automate.attr('node', shape='doublecircle')
                for final_state in graph['accepting_states']:
                    automate.node(final_state)

                automate.attr('node', shape='circle')
                for state in graph['transitions']:
                    automate.edge(state[0], state[2], label=state[1])
                automate.view()

    # f.attr(rankdir='LR', size='8,5')
