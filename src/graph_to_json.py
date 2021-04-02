from Parser import *
import os
import json


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
    # print(
    #     '_____________________________________________\n___________________________________')
    return gr


def write_to_json_file(name, json_graph):
    # Créer un fichier json contenant le langage lu
    with open(os.path.join(os.getcwd(), "..\\Results\\" + name), 'w') as outfile:
        json.dump(json_graph, outfile, indent=2)
        outfile.close()
