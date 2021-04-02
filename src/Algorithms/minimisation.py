import collections
from itertools import combinations
from Node import Node
from Parser import Parser


def minimisation(graph):
    """Fonction de minimisation d'un automate

    Algorithme calculant un automate déterministe minimal équivalent au premier.

    """
    print("min")
    final_states = graph.getFinalStates()
    states = graph.getStates()
    alphabet = graph.getAlphabet()
    partitions = [[], []]
    # Créer la partition initiale P0 = { {état finaux}, {états non finaux} }
    for state in states:
        if state in final_states:
            partitions[0].append(state)
        else:
            partitions[1].append(state)

    i = 0
    while (i < len(partitions)):
        # Récupérer les pairs des éléments de la partition
        pairs = list(combinations(partitions[i], 2))
        print(i, partitions[i])
        distinguishable = False
        for p in pairs:
            if distinguishable:
                break
            print(p)
            # print(p[0])
            for x in alphabet:
                # Récupérer les transitions possibles depuis la paire d'états avec la lettre x
                t1 = graph.getStateTransitionsLetter(p[0], x)
                t2 = graph.getStateTransitionsLetter(p[1], x)
                if (len(t1) == 0 or len(t2) == 0):
                    # distinguishable = False
                    if p[1] in partitions[i]:
                        partitions[i].remove(p[1])
                        partitions.append(list(p[1]))
                else:
                    l1 = []
                    l2 = []
                    for l in partitions:
                        if (t1[0].mGoto in l):
                            l1 = l
                        if (t2[0].mGoto in l):
                            l2 = l

                    # print(l1)
                    # print(l2)
                    # print("__________")
                    # Si les états d'arrivée des 2 noeuds sont dans 2 partitions différentes
                    # Alors séparer les états dans la liste des partitions
                    if (l1 and l2 and l1 != l2):
                        distinguishable = True
                        if p[1] in partitions[i]:
                            partitions[i].remove(p[1])
                            partitions.append(list(p[1]))
                        # Révenir au début de la liste des partitions car changement
                        i = 0
                        break
                    else:
                        distinguishable = False

        i = i + 1
    # Construire le graphe minimal
    graph_min = Parser()
    for p in partitions:
        ns = ",".join(p)
        graph_min.states.append(ns)
        for fs in graph.finalStates:
            if fs in p and ns not in graph_min.finalStates:
                graph_min.finalStates.append(ns)
        # print(",".join(p))

    # for state in graph_min.states:
    for node in graph.Nodes:
        for p in partitions:
            if node.mFrom in p:
                i = partitions.index(p)
            if node.mGoto in p:
                j = partitions.index(p)
        new_node = Node(graph_min.states[i],
                        node.mValue, graph_min.states[j])
        if (new_node not in graph_min.Nodes):
            graph_min.Nodes.append(new_node)
    graph_min.initialState = graph_min.states[0]
    return graph_min
