import collections
from itertools import combinations
from src.Transition import Transition
from src.Graph import Graph


def minimisation(graph):
    """Fonction de minimisation d'un automate.

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
    print(partitions)
    i = 0
    while (i < len(partitions)):
        # Récupérer les pairs des éléments de la partition
        pairs = list(combinations(partitions[i], 2))
        distinguishable = False
        for p in pairs:
            if distinguishable:
                break
            for letter in alphabet:
                # Récupérer les transitions possibles depuis la paire d'états avec la lettre
                t1 = graph.getStateTransitionsLetter(p[0], letter)
                t2 = graph.getStateTransitionsLetter(p[1], letter)

                if (len(t1) == 0 or len(t2) == 0):
                    distinguishable = False
                elif (len(t1) != 0 and len(t2) == 0):
                    x = -1
                    for j in range(len(partitions)):
                        if (t1[0].mGoto in partitions[j]):
                            x = j
                    distinguishable = True
                    partitions[i].remove(p[0])
                    partitions.append(list(p[0]))

                elif (len(t1) == 0 and len(t2) != 0):
                    x = -1
                    for j in range(len(partitions)):
                        if (t2[0].mGoto in partitions[j]):
                            x = j
                    distinguishable = True
                    partitions[i].remove(p[1])
                    partitions.append(list(p[1]))
                else:
                    x = -1
                    y = -1
                    for j in range(len(partitions)):
                        if (t1[0].mGoto in partitions[j]):
                            x = j
                        if (t2[0].mGoto in partitions[j]):
                            y = j
                    # Si les états d'arrivée des 2 noeuds sont dans 2 partitions différentes
                    # Alors séparer les états dans la liste des partitions*
                    if x != -1 and y != -1 and x != y:
                        distinguishable = True
                        print(partitions, ' || ', p[1], ' || ', i)
                        partitions[i].remove(p[1])
                        partitions.append(list(p[1]))
                        # Révenir au début de la liste des partitions car changement
                        i = 0
                        break
                    else:
                        distinguishable = False

        i = i + 1
    print(partitions)
    # Construire le graphe minimal
    graph_min = Graph()
    for p in range(len(partitions)):
        graph_min.states.append(str(p+1))
        for fs in graph.finalStates:
            if fs in partitions[p]:
                graph_min.finalStates.append(str(p+1))
                break

    for state in graph.states:
        for i in range(len(partitions)):
            # Groupe de l'état source
            if state in partitions[i]:
                x = i
                break

        trans = graph.getStateTransitions(state)
        for tr in trans:
            # Groupe de l'état destination
            for j in range(len(partitions)):
                if tr.mGoto in partitions[j]:
                    y = j
                    break
            # Nouvelle transition entre deux groupes dans l'automate minimal
            new = Transition(str(x + 1), tr.mValue, str(y + 1))
            if new not in graph_min.transitions:
                graph_min.transitions.append(new)

    for i in range(len(partitions)):
        if graph.initialState in partitions[i]:
            k = i
            break
    graph_min.initialState = str(k + 1)

    return graph_min
