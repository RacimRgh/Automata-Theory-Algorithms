#
#   Python DFA
#
from Graph import *
from Parser import *
from Algorithms import *
import json
import glob
import os
from os import listdir
from os.path import isfile, join
from pathlib import Path


def main():
    path = Path('..\\Files\\')
    input_files = (
        entry for entry in path.iterdir() if entry.is_file())

    # for item in input_files:
    #     print(item)

    # Parcours récursif de tout les fichiers dans le dossier Files
    # 1 fichier == 1 langage/graphe
    # for filename in glob.glob(os.path.join(path, '*.txt')):
    for filename in input_files:
        with open(os.path.join(os.getcwd(), filename), 'r') as f:  # ouvrir en mode lecture
            print(filename)
            name = filename.name.split('.')[0] + '.json'
            print(name)

            # parse le fichier et récupérer l'alphabet, les noeuds et états finaux
            parsedFile = Parser(f)
            parsedFile.parse()

            # Récupérer les transitions
            # [ ["from", "value", "to"], .... ["from","value", "to"] ]
            nodes = parsedFile.getNodes()
            nodes = [[str(node.mFrom), str(node.mValue), str(node.mGoto)]
                     for node in nodes]
            # print(nodes)
            finalStates = parsedFile.getFinalStates()
            # print(finalStates)
            alphabet = parsedFile.getAlphabet()
            # print(alphabet)

            gr = {}
            gr['alphabet'] = alphabet
            gr['states'] = finalStates
            gr['initial_state'] = finalStates
            gr['accepting_states'] = finalStates
            gr['transitions'] = nodes
            print(
                '_____________________________________________\n___________________________________')

            with open(os.path.join(os.getcwd(), "..\\Results\\"+name), 'w') as outfile:
                json.dump(gr, outfile)

            Algorithms(parsedFile)


if __name__ == '__main__':
    main()
