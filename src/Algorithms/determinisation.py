import queue
from Node import Node
from Parser import Parser


def ajout_trans(noeud, graph):
    if noeud not in graph.Nodes:
        graph.Nodes.append(noeud)
    return graph.Nodes


def determinisation(graph):
    """Fonction de déterminisation d'un automate

    Algorithme calculant un automate déterministe équivalent au premier.

    """
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
