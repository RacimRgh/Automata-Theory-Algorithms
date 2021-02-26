#
#   Python DFA
#
from Parser import Parser
from Algorithms import *
import json
import os
from os import listdir
from os.path import isfile, join
from pathlib import Path


def main():
    path = Path('..\\Files\\')
    input_files = (
        entry for entry in path.iterdir() if entry.is_file())

    # Parcours récursif de tout les fichiers dans le dossier Files
    # 1 fichier == 1 langage/graphe
    for filename in input_files:
        with open(os.path.join(os.getcwd(), filename), 'r') as f:  # ouvrir en mode lecture
            print(filename)
            name = filename.name.split('.')[0] + '.json'
            print(name)

            # parse le fichier et récupérer l'alphabet, les noeuds et états finaux
            parsedFile = Parser(f)
            parsedFile.parse()

            initialState = parsedFile.getInitialState()
            print('Etat initial: ', initialState)

            finalStates = parsedFile.getFinalStates()
            print('Etats finaux: ', finalStates)

            alphabet = parsedFile.getAlphabet()
            print('Alphabet: ', alphabet)

            states = parsedFile.getStates()
            print('Etats: ', states)

            # Récupérer les transitions
            # [ ["from", "value", "to"], .... ["from","value", "to"] ]
            nodes = parsedFile.getNodes()
            nodes = [[str(node.mFrom), str(node.mValue), str(node.mGoto)]
                     for node in nodes]
            print('Transitions:', nodes)

            gr = {}
            gr['alphabet'] = alphabet
            gr['states'] = states
            gr['initial_state'] = initialState
            gr['accepting_states'] = finalStates
            gr['transitions'] = nodes
            print(
                '_____________________________________________\n___________________________________')

            # Créer un fichier json contenant le langage lu
            with open(os.path.join(os.getcwd(), "..\\Results\\"+name), 'w') as outfile:
                json.dump(gr, outfile)

            # Exécuter les algorithmes
            # TO DO
            Algorithms(parsedFile)


if __name__ == '__main__':
    main()
