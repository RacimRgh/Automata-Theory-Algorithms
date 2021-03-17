from Node import *
from Parser import *
from MainEntry import getgraph, write_to_json_file
import random
from random import seed
from random import choice
from string import ascii_lowercase


def generate_lang():
    n_states = random.randint(3, 8)
    n_alphabet = random.randint(2, 5)
    n_finaux = random.randint(1, 3)
    graph = Parser()

    for i in range(n_alphabet):
        graph.alphabet.append(ascii_lowercase[i])

    for i in range(n_states):
        graph.states.append(str(i+1))
        for x in graph.alphabet:
            for j in range(n_states+1):
                graph.Nodes.append(Node(str(i), x, str(j)))
    for i in range(n_finaux):
        select_fin = choice(graph.states)
        if select_fin not in graph.finalStates:
            graph.finalStates.append(select_fin)

    graph.initialState = choice(graph.states)

    print(len(graph.Nodes))
    seed(1)
    to_del = len(graph.Nodes) - int(len(graph.Nodes) * 0.2)
    print("Del: ", to_del)
    for i in range(to_del):
        select_del = choice(graph.Nodes)
        graph.Nodes.remove(select_del)

    # for tr in graph.Nodes:
    #     print(graph.nodeToString(tr))
    print(len(graph.Nodes))
    return graph


g = generate_lang()
json_graph = getgraph(g)
write_to_json_file("gen.json", json_graph)
