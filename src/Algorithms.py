from Parser import *
from Node import *
import collections
import queue
from itertools import combinations

# algorithme prenant un automate déterministe et un mot, et décidant si le mot est accepté par l'automate.


def acceptation(graph):
    # parse file and store states
    nodes = graph.getNodes()
    finalStates = graph.getFinalStates()
    alphabet = graph.getAlphabet()
    initialState = graph.getInitialState()
    # print(initialState)
    # get string to check against
    running = True
    while(running):
        uInput = input("Please enter string or quit: ")
        if (uInput == "quit"):
            running = False
        else:
            mot = uInput
            print(mot)
            mot = mot + mot[-1]
            currentNode = initialState
            error = False
            counter = 0
            for letter in mot:
                # Vérifier si la lettre est dans l'alphabet
                if letter in alphabet:
                    # Vérifier si la lettre est dans le noeud courant
                    for node in nodes:
                        # print(type(str(node.mFrom)), type(currentNode))
                        if node.mFrom == currentNode and node.mValue == letter:
                            print("Read {} from {} to {}".format(
                                node.mValue, node.mFrom, node.mGoto))
                            # Si c'est la dernière lettre du mot
                            if (counter == len(mot) - 1):
                                # Si état final alors mot accepté
                                if (currentNode in finalStates):
                                    break
                                else:
                                    print(
                                        "Error last letter not in final state")
                                    error = True
                                    break
                            # Avencer le noeud
                            currentNode = node.mGoto
                            break
                # Si mot pas dans le langage
                else:
                    print("Error letter not in alphabet")
                    error = True
                    break
                counter += 1
            if (error):
                print("Not valid!")
            else:
                print("String accepted")

# algorithme calculant un automate équivalent au premier, sans "epsilon-transitions".


def synchronisation(graph):
    print("syncho")
    nodes = graph.getNodes()
    # alphabet = graph.getAlphabet()
    for node in nodes:
        if node.mValue == "\u03b5":
            epsilonTransitions = graph.getStateTransitions(
                node.mGoto)
            for epsilonNode in epsilonTransitions:
                print(graph.nodeToString(epsilonNode))
                nodes.append(
                    Node(node.mFrom, epsilonNode.mValue, epsilonNode.mGoto))
                # algorithme calculant un automate déterministe équivalent au premier.
            nodes.remove(node)
    return graph


# Vérifier si l'état existe déjà
# Cas particuliers à traiter:
#                   -0124 et 4201 sont le même état
#                   -124 et 0124 ne sont pas le même
def containsAll(states, new_st):
    for st in states:
        if len(st) != len(new_st):
            continue
        else:
            if 0 not in [c in st for c in new_st]:
                return 1
    return 0


def ajout_trans(noeud, graph):
    if noeud not in graph.Nodes:
        graph.Nodes.append(noeud)
    return graph.Nodes

# algorithme calculant un automate déterministe équivalent au premier.


def determinisation(graph):
    print("determinisation")

    # Automate non déterministe
    currentNode = graph.getInitialState()
    alphabet = graph.getAlphabet()

    graph_org = graph

    # File pour le traitement des noeuds
    states_queue = queue.Queue()
    states_queue.put(currentNode)

    # Noeuds traités
    state_done = []
    # File des noeuds non traités
    while (not states_queue.empty()):
        currentNode = states_queue.get()
        if (currentNode not in state_done):
            print("____________________________________________________________")
            print(currentNode)
            for letter in alphabet:
                # on parcours les transitions depuis l'état en cours de traitement
                # récupérer la liste des transitions possible depuis l'état actuel en lisant la lettre actuelle
                current_node_transitions = graph.getStateTransitions(
                    currentNode)
                current_node_transitions = [
                    tr for tr in current_node_transitions if tr.mValue == letter]

                ############## TEST ###############
                print('Transitions possibles: ')
                for tr in current_node_transitions:
                    print(graph.nodeToString(tr))
                ###################################

                if len(current_node_transitions):
                    # liste des transitions non déterministes
                    # (ie: plusieurs déplacements possibles avec la même lettre depuis un état)

                    # non_det_trans = [
                    #     tr for tr in current_node_transitions
                    #     if current_node_transitions.count(tr) > 1]

                    ############## TEST ###############
                    # print('Non det: ')
                    # for tr in non_det_trans:
                    #     print(graph.nodeToString(tr))
                    ###################################

                    # Si pas de non déterminisme, ajouter les succésseurs à la liste des états à traiter
                    # if len(non_det_trans) == 0:
                    if len(current_node_transitions) == 1:
                        for n in current_node_transitions:
                            states_queue.put(n.mGoto)

                    # si liste des dupliqués non vide alors déterminiser
                    # parcourir la liste des transitions non déterministes de l'état courant
                    # ajouter un nouvel état
                    else:
                        new_state = ''
                        # Nom du nouvel état
                        # for trans in non_det_trans:
                        for trans in current_node_transitions:
                            if len(trans.mGoto) > 1:
                                for t in trans.mGoto:
                                    if t not in new_state:
                                        new_state += t
                            else:
                                if(trans.mGoto not in new_state):
                                    new_state += trans.mGoto

                        # Trier par ordre alphabétique le nouvel état
                        # print(sorted(new_state))
                        new_state = "".join(sorted(new_state))
                        # ajouter le nouvel état
                        # if not containsAll(graph.states, new_state):
                        if new_state not in graph.states:
                            graph.states.append(new_state)
                            # Transitions non déterministes
                            # for trans in non_det_trans:
                            for trans in current_node_transitions:
                                # print(graph.nodeToString(trans))
                                goto_nodes = graph.getStateTransitions(
                                    trans.mGoto)
                                # Récupérer les succésseurs des états non déterministes
                                print('\n*******Trans:')
                                for gtn in goto_nodes:
                                    print(graph.nodeToString(gtn))
                                    if gtn in graph_org.Nodes:
                                        new_trans = Node(
                                            new_state, gtn.mValue, gtn.mGoto)
                                        graph.Nodes = ajout_trans(
                                            new_trans, graph)
                                    # print(graph.nodeToString(gtn))

                                graph.Nodes.remove(trans)

                            # Ajouter les nouvelles transitions et nouvel état au graphe
                            graph.Nodes = ajout_trans(
                                Node(currentNode, trans.mValue, new_state), graph)
                            states_queue.put(new_state)
                        else:
                            # for trans in non_det_trans:
                            for trans in current_node_transitions:
                                goto_nodes = graph.getStateTransitions(
                                    trans.mGoto)
                                graph.Nodes.remove(trans)
                                new_trans = Node(
                                    currentNode, trans.mValue, new_state)
                                graph.Nodes = ajout_trans(
                                    new_trans, graph)

            # Etat traité
            state_done.append(currentNode)
    # Calcul des états finaux
    for state in graph.states:
        for final in graph.finalStates:
            if final in state:
                graph.finalStates.append(state)
                break
    return graph

# algorithme calculant un automate déterministe minimal équivalent au premier.


def minimisation(graph):
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
        for p in pairs:
            # print(p[0])
            for x in alphabet:
                # Récupérer les transitions possibles depuis la paire d'états avec la lettre x
                t1 = graph.getStateTransitionsLetter(p[0], x)
                t2 = graph.getStateTransitionsLetter(p[1], x)
                if (len(t1) == 0 or len(t2) == 0):
                    distinguishable = False
                else:
                    for l in partitions:
                        if (t1[0].mGoto in l):
                            l1 = l
                        if (t2[0].mGoto in l):
                            l2 = l
                    # Si les états d'arrivée des 2 noeuds sont dans 2 partitions différentes
                    # Alors séparer les états dans la liste des partitions
                    if (l1 != l2):
                        distinguishable = True
                        partitions[i].remove(p[1])
                        partitions.append(list(p[1]))
                        # Révenir au début de la liste des partitions car changement
                        i = 1
                    else:
                        distinguishable = False
                        i += 1
    # Construire le graphe minimal
    graph_min = Parser()
    for p in partitions:
        graph_min.states.append(",".join(p))
        print(",".join(p))

    # for state in graph_min.states:
    graph_min.initialState = graph_min.states[0]
    graph_min.finalStates.append(graph_min.states[1])
    graph_min.Nodes.append(Node(graph_min.states[0], 'a', graph_min.states[0]))
    graph_min.Nodes.append(Node(graph_min.states[0], 'b', graph_min.states[1]))
    return graph_min


# algorithme prenant deux automates, et déterminant si ceux-ci sont équivalents.
def equivalence(graph):
    print("eq")

# algorithme prenant une expression régulière, et retournant l'automate de Thompson calculant le langage correspondant à cette expression.


def thompson(graph):
    print("thomson")
