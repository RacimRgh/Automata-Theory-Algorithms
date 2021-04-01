#
#   Python DFA
#
from Parser import Parser
from Algorithms import acceptation, determinisation, synchronisation, minimisation
from Automate_from_json import generate_automate
from Random_lang import generate_lang, isolated_node
import json
import os
from os import listdir
from os.path import isfile, join
from pathlib import Path
import codecs


def getgraph(graph):
    initial_state = graph.getInitialState()
    # print('Etat initial: ', initial_state)

    final_states = graph.getFinalStates()
    # print('Etats finaux: ', final_states)

    alphabet = graph.getAlphabet()
    # print('Alphabet: ', alphabet)

    states = graph.getStates()
    # print('Etats: ', states)
    # Récupérer les transitions
    # [ ["from", "value", "to"], .... ["from","value", "to"] ]
    nodes = graph.getNodes()
    nodes = [[str(node.mFrom), str(node.mValue), str(node.mGoto)]
             for node in nodes]
    # for node in nodes:
    # print(node)
    # print('Transitions:', nodes)

    gr = {'alphabet': alphabet, 'states': states, 'initial_state': initial_state, 'accepting_states': final_states,
          'transitions': nodes}
    print(
        '_____________________________________________\n___________________________________')
    return gr


def write_to_json_file(name, json_graph):
    # Créer un fichier json contenant le langage lu
    with open(os.path.join(os.getcwd(), "..\\Results\\" + name), 'w') as outfile:
        json.dump(json_graph, outfile, indent=2)
        outfile.close()


def main():
    i = 1
    files_path = Path('..\\Files\\')

    while i < 3:
        filename = "Ex1-" + str(i)
        with open(os.path.join(os.getcwd(), '..\\Files\\' + filename + ".txt"), 'w') as outfile:
            g = generate_lang()
            # isolated = isolated_node(g)
            # if isolated == False:
            final = " ".join(g.finalStates) + "\n"
            outfile.write(final)
            for node in g.Nodes:
                outfile.write(
                    " ".join([node.mFrom, node.mValue, node.mGoto]) + "\n")
            i = i + 1
            outfile.close()
            json_graph = getgraph(g)
            write_to_json_file(filename + ".json", json_graph)
            # else:
            #     continue

    input_files = (
        entry for entry in files_path.iterdir() if entry.is_file())

    # Parcours récursif de tout les fichiers dans le dossier Files
    # 1 fichier == 1 langage/graphe
    for filename in input_files:
        # ouvrir en mode lecture
        with codecs.open(os.path.join(os.getcwd(), filename), encoding='utf-8') as f:
            # parse le fichier et récupérer l'alphabet, les noeuds et états finaux
            graph = Parser(f)
            graph.parse()
            num_exo = filename.name.split('.')[0]
            name = filename.name.split('.')[0] + '.json'
            print(name)

            json_graph = getgraph(graph)
            write_to_json_file(name, json_graph)

            # Exécuter les algorithmes
            # determinisation
            # det = determinisation(graph)
            # det_json = getgraph(det)
            # write_to_json_file(num_exo+"-det.json", det_json)

            # gmin = minimisation(det)
            # gmin_json = getgraph(gmin)
            # write_to_json_file(num_exo+"-min.json", gmin_json)

            # gmin = minimisation(graph)
            # gmin_json = getgraph(gmin)
            # write_to_json_file("min.json", gmin_json)

            # acceptation
            # algos.acceptation()

            # synchronisation
            # eps = algos.synchronisation()
            # eps_json = getgraph(eps)
            # write_to_json_file("abab-sans-epsilon.json", eps_json)
    generate_automate()


if __name__ == '__main__':
    main()
