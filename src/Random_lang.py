from Node import *
from Parser import *
# from MainEntry import getgraph, write_to_json_file
import random
from random import seed
from random import choice
from string import ascii_lowercase
import os


def isolated_node(g):
    # destinations = [node.mGoto for node in g.Nodes]
    # sources = [node.mFrom for node in g.Nodes]
    for state in g.states:
        sources = []
        destinations = []
        destinations = [
            node.mGoto for node in g.Nodes if node.mFrom == state]
        sources = [node.mFrom for node in g.Nodes if node.mGoto == state]

        print(state, ' : destinations: ', destinations)
        print(state, ' : sources: ', sources)

        # Etat initial sans succéssseur à part lui même
        if (state == g.initialState):
            if (len(destinations) == 0 or (len(destinations) == 1 and destinations[0] == state)):
                print('\nHERE\n')
                return False

        # Etat final sans prédécesseur à part lui même
        if (state in g.finalStates):
            if (len(sources) == 0 or (len(sources) == 1 and sources[0] == state)):
                print('\nHERE1\n')
                return False

        # Etat sans successeur et pas final
        if ((len(destinations) == 0 or (len(destinations) == 1 and destinations[0] == state)) and state not in g.finalStates):
            print('\nHERE2\n')
            return False

        # Etat isolé
        node_sources = []
        node_destinations = []
        node_destinations = [node.mGoto for node in g.Nodes]
        node_sources = [node.mFrom for node in g.Nodes]
        if ((state not in node_destinations) and (state not in node_sources)):
            print('\nHERE3\n')
            return False

        # # Etat source, sans noeud qui y va, et n'est pas initial = inaccessible
        # elif (state in sources) and (state not in destinations) and (state != g.initialState):
        #     return False
    return True
    # for state in g.states:
    #     n = 0
    #     for node in g.Nodes:
    #         # état final sans successeur
    #         if state in g.finalStates and


def generate_lang():
    repeat = False
    while repeat == False:

        n_states = random.randint(3, 8)
        n_alphabet = random.randint(2, 4)
        n_finaux = random.randint(1, 3)
        n_nodes = random.randint(7, 14)
        graph = Parser()

        # Générer les lettres de l'alphabet
        for i in range(n_alphabet):
            graph.alphabet.append(ascii_lowercase[i])

        # Générer les états et les noeuds de l'automate
        for i in range(n_states):
            graph.states.append(str(i+1))
            for x in graph.alphabet:
                for j in range(n_states+1):
                    graph.Nodes.append(Node(str(i), x, str(j)))

        # Choisir les états finaux de l'automate
        for i in range(n_finaux):
            select_fin = choice(graph.states)
            if select_fin not in graph.finalStates:
                graph.finalStates.append(select_fin)

        graph.initialState = choice(graph.states)

        while(len(graph.Nodes) > n_nodes):
            select_del = choice(graph.Nodes)
            graph.Nodes.remove(select_del)

        repeat = isolated_node(graph)
    # for tr in graph.Nodes:
    #     print(graph.nodeToString(tr))
    # print(len(graph.Nodes))
    return graph
