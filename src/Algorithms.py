from Node import *
import collections
import queue


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

# algorithme calculant un automate déterministe équivalent au premier.


def determinisation(graph):
    print("determinisation")
    nodes = graph.getNodes()
    currentNode = graph.getInitialState()
    states = graph.getStates()
    states_queue = queue.Queue()
    states_queue.put(currentNode)
    node_treated = []
    while (not states_queue.empty()):
        currentNode = states_queue.get()
        for node in nodes:
            # on parcours les transitions depuis l'état en cours de traitement
            if node.mFrom == currentNode and node not in node_treated:
                # récupérer la liste des transitions possible depuis l'état actuel
                current_node_transitions = graph.getStateTransitions(
                    node.mFrom)
                # liste des transitions non déterministes
                # (ie: plusieurs déplacements possibles avec la même lettre depuis un état)
                non_det_trans = [
                    tr for tr in current_node_transitions if current_node_transitions.count(tr) > 1]

                # si liste des dupliqués non vide alors déterminiser
                # parcourir la liste des transitions non déterministes de l'état courant
                # ajouter un nouvel état
                if len(non_det_trans):
                    new_state = ''
                    for trans in non_det_trans:
                        new_state += trans.mGoto
                        nodes.remove(trans)
                        print(graph.nodeToString(trans))
                    print(new_state)
                    states.append(new_state)
                    nodes.append(
                        Node(currentNode, trans.mValue, new_state))
                    states_queue.put(new_state)
                # Sinon ajout les succésseurs à la liste des états à traiter
                else:
                    states_queue.put(node.mGoto)

                currentNode = node.mGoto
                node_treated.append(node)
        for node in nodes:
            print(graph.nodeToString(node))
    return graph

# algorithme calculant un automate déterministe minimal équivalent au premier.


def minimisation(graph):
    print("min")

# algorithme prenant deux automates, et déterminant si ceux-ci sont équivalents.


def equivalence(graph):
    print("eq")

# algorithme prenant une expression régulière, et retournant l'automate de Thompson calculant le langage correspondant à cette expression.


def thompson(graph):
    print("thomson")
