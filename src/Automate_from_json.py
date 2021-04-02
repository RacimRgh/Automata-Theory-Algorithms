"""Module de génération d'images d'automates

Ce module utilise la librairie graphviz, et les fichiers JSON
situés dans le dossier 'Results' pour générer des images
contenant des automates
https://graphviz.readthedocs.io/en/stable/

"""
from graphviz import Digraph
import json
from pathlib import Path
import os


def generate_automate():
    """Fonction de génération d'images d'Automates

    La fonction parcours tout le dossier 'Results', et récupère seulement
    les fichier JSON. Puis utilise la classe Diagraph de la librarie graphviz
    pour générer une image png de l'automate.

    Note:
        L'état initial est représenté sous la forme d'un oeuf dû
        à l'absence de représentation par une flèche.

    Todo:
        * Trouver un moyen de mieux représenter l'état initial

    """
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
