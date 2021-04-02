from Parser import *
from Node import *
from graph_to_json import getgraph, write_to_json_file
from collections import deque
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


# # Vérifier si l'état existe déjà
# # Cas particuliers à traiter:
# #                   -0124 et 4201 sont le même état
# #                   -124 et 0124 ne sont pas le même
# def containsAll(states, new_st):
#     for st in states:
#         if len(st) != len(new_st):
#             continue
#         else:
#             if 0 not in [c in st for c in new_st]:
#                 return 1
#     return 0


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


# algorithme prenant deux automates, et déterminant si ceux-ci sont équivalents.
def equivalence(graph):
    print("eq")

# algorithme prenant une expression régulière, et retournant l'automate de Thompson calculant le langage correspondant à cette expression.


def gen_state(states):
    for i in range(100):
        if str(i) not in states:
            return str(i)


def prefix_regex(exp):
    prio = {
        ')': 0,
        '(': 0,
        '*': 3,
        '.': 1,
        '+': 1,
        '?': 1
    }
    operators = ['*', '.', '+']
    # op_stack = deque()
    # out_stack = deque()
    op_stack = []
    out_stack = []
    print("thomson")
    for c in exp:
        # Si le caractère lu n'est ni opérateur ni ( )
        # L'ajoute à la pile de sortie
        if c not in prio.keys():
            # print('1-', c)
            out_stack.append(c)

        # Si le caractère est un opérateur
        elif c in operators:
            # print('2-', c)
            # 1 - Si le sommet est un opérateur avec une + grande priorité
            if len(op_stack) > 0:
                top = op_stack.pop()
                while top in operators and prio[top] >= prio[c]:
                    out_stack.append(top)
                    # Parcours la pile tant que le sommet est un opérateur
                    # et est plus prioritaire que la caractère lu
                    # while (len(op_stack) > 0):
                    if (len(op_stack) == 0):
                        break
                    top = op_stack.pop()
                    if (top in operators and prio[top] < prio[c]) or top not in operators:
                        break
                    # out_stack.append(top)
                # Si le caractère lu est un opérateur, et le sommet de pile est une '('
                if top in operators and prio[top] < prio[c]:
                    op_stack.append(top)
                    op_stack.append(c)
                if top == '(':
                    op_stack.append(top)
                    op_stack.append(c)
                if (len(op_stack) == 0):
                    op_stack.append(c)
            else:
                op_stack.append(c)

        # Si le caractère lu est une '('
        elif c == '(':
            # print('3-', c)
            op_stack.append(c)

        # Si le caractère lu == ')': dépiler tout les opérateurs jusqu'à arriver à '('
        elif c == ')':
            # print('4-', c)
            if (len(op_stack) > 0):
                top = op_stack.pop()
                if top in operators:
                    out_stack.append(top)
                    while (len(op_stack) > 0):
                        top = op_stack.pop()
                        if top == '(':
                            break
                        out_stack.append(top)
                else:
                    print('Mauvaise expression.')
    for op in op_stack:
        out_stack.append(op)
    return out_stack


def thompson(exp):
    out_stack = prefix_regex(exp)
    print(out_stack)
    graph_stack = []
    thompson_graph = Parser()
    operators = ['*', '.', '+']
    states = []
    for c in out_stack:
        # Si c'est un caractère
        # Créer un graphe avec un etat initial et etat final, et transition en lisant c
        if c not in operators:
            print("1-", c)
            g = Parser()
            print(len(graph_stack))

            g.alphabet.append(c)  # ajouter la lettre à l'alphabet

            i = gen_state(states)  # générer l'état initial
            states.append(i)
            g.initialState = i
            g.states.append(i)

            j = gen_state(states)  # générer l'état final
            states.append(j)
            g.finalStates.append(j)
            g.states.append(j)

            # ajouter la transition (initial, c, final)
            g.Nodes.append(Node(i, c, j))
            # ajouter le graphe à la pile
            graph_stack.append(g)
        # Si
        elif c == '*':
            print("2-", c)
            g = Parser()
            g = graph_stack.pop()  # récupérer le dernier graphe dans la pile
            print(len(graph_stack))

            g.Nodes.append(Node(g.finalStates[0], '\u03b5', g.initialState))

            i = gen_state(states)  # générer l'état initial
            g.states.append(i)
            states.append(i)
            g.Nodes.append(Node(i, '\u03b5', g.initialState))
            g.initialState = i

            j = gen_state(states)  # générer l'état final
            g.states.append(j)
            states.append(j)
            g.Nodes.append(Node(g.finalStates[0], '\u03b5', j))
            g.finalStates = []
            g.finalStates.append(j)
            g.Nodes.append(Node(g.initialState, '\u03b5', g.finalStates[0]))

            graph_stack.append(g)
        # Si
        elif c == '+':
            print("3-", c)
            print(len(graph_stack))
            g1 = graph_stack.pop()
            g2 = graph_stack.pop()
            g = Parser()

            g.states = list(set().union(g1.states, g2.states))
            # g.states = [state for state in g1.states if state not in g.states]
            # g.states = [state for state in g2.states if state not in g.states]
            g.alphabet = list(set().union(g1.alphabet, g2.alphabet))
            # g.alphabet = [c for c in g1.alphabet if c not in g.alphabet]
            # g.alphabet = [c for c in g2.alphabet if c not in g.alphabet]
            for node in g1.Nodes:
                g.Nodes.append(node)
            for node in g2.Nodes:
                g.Nodes.append(node)

            i = gen_state(states)  # générer l'état initial
            g.states.append(i)
            states.append(i)
            g.Nodes.append(Node(i, '\u03b5', g1.initialState))
            g.Nodes.append(Node(i, '\u03b5', g2.initialState))
            g.initialState = i

            j = gen_state(states)  # générer l'état final
            g.states.append(j)
            states.append(j)
            g.Nodes.append(Node(g1.finalStates[0], '\u03b5', j))
            g.Nodes.append(Node(g2.finalStates[0], '\u03b5', j))
            g.finalStates = []
            g.finalStates.append(j)

            graph_stack.append(g)
        # si
        elif c == '.':
            print("4-", c)
            print(len(graph_stack))
            g1 = graph_stack.pop()
            g2 = graph_stack.pop()
            g = Parser()

            g.Nodes = [node for node in g2.Nodes]
            g.alphabet = list(set().union(g1.alphabet, g2.alphabet))
            g.states = [
                state for state in g1.states if state not in g.states and state != g1.initialState]
            g.states = list(set().union(g.states, g2.states))

            g.initialState = g2.initialState
            g.finalStates.append(g1.finalStates[0])

            for node in g1.Nodes:
                if node.mFrom != g1.initialState:
                    g.Nodes.append(node)
                else:
                    g.Nodes.append(
                        Node(g2.finalStates[0], node.mValue, node.mGoto))
            graph_stack.append(g)

    thompson_graph = graph_stack.pop()
    return thompson_graph
