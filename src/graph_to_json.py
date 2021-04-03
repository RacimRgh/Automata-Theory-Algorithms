"""Module pour transformer un graphe en dictionnaire et fichier json
    
"""
from src.Graph import *
import os
import json


def getgraph(graph):
    """Fonction qui transforme un objet graphe en dictionnaire python.

    Cette fonction prend un graphe en paramètre et le transforme en
    dictionnaire suivant la syntaxe des fichiers JSON de la librairie graphviz.

    Args:
        graph (Graph): Un objet graphe de la classe Graph.

    Returns:
        dict: Un dictionnaire représentant le graphe.
    """
    initial_state = graph.getInitialState()

    final_states = graph.getFinalStates()

    alphabet = graph.getAlphabet()

    states = graph.getStates()
    # Récupérer les transitions
    # [ ["from", "value", "to"], .. ["from","value", "to"] ]
    nodes = graph.getNodes()
    nodes = [[str(node.mFrom), str(node.mValue), str(node.mGoto)]
             for node in nodes]

    gr = {
        'alphabet': alphabet,
        'states': states,
        'initial_state': initial_state,
        'accepting_states': final_states,
        'transitions': nodes
    }

    return gr


def write_to_json_file(name, json_graph):
    """ Créer un fichier json contenant un langage

    Fonction qui crée un fichier JSON dans le dossier 'Results'
    contenant un graphe sous la syntaxe JSON de graphviz

    Args:
        name (str): Nom du fichier JSON à enregistrer
        json_graph (dict): Dictionnaire qui décrit un graphe.
    """
    with open(os.path.join(os.getcwd(), ".\\Results\\" + name), 'w') as outfile:
        json.dump(json_graph, outfile, indent=2)
        outfile.close()
