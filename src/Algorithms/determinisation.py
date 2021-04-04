import queue
from src.Transition import Transition
from src.Graph import Graph


def ajout_trans(noeud, graph):
    if noeud not in graph.transitions:
        graph.transitions.append(noeud)
    return graph.transitions


def determinisation(graph):
    """Fonction de déterminisation d'un automate

    Algorithme calculant un automate déterministe équivalent au premier.

    Returns:
        Graph: un automate déterministe

    """
    print("determinisation")

    # Automate non déterministe
    currentTransition = graph.getInitialState()
    alphabet = graph.getAlphabet()

    graph_org = graph

    # File pour le traitement des noeuds
    states_queue = queue.Queue()
    states_queue.put(currentTransition)

    # Noeuds traités
    state_done = []

    # File des noeuds non traités
    while (not states_queue.empty()):
        currentTransition = states_queue.get()
        if (currentTransition not in state_done):

            ############## TEST ###############
            print("____________________________________________________________")
            print(currentTransition)
            ############## TEST ###############

            for letter in alphabet:
                # on parcours les transitions depuis l'état en cours de traitement
                # récupérer la liste des transitions possible depuis l'état actuel en lisant la lettre actuelle
                current_node_transitions = graph.getStateTransitionsLetter(
                    currentTransition, letter)

                ############## TEST ###############
                # print('Transitions possibles: ')
                # for tr in current_node_transitions:
                #     print(graph.nodeToString(tr))
                ############## TEST ###############

                # Si on trouve des transitions possibles depuis l'état courant en lisant la lettre courante
                if len(current_node_transitions):
                    # Si pas de non déterminisme
                    # (ie: plusieurs déplacements possibles avec la même lettre depuis un état)
                    # ajouter les succésseurs à la liste des états à traiter
                    if len(current_node_transitions) == 1:
                        for n in current_node_transitions:
                            states_queue.put(n.mGoto)

                    # Si plusieurs transitions possibles avec une lettre et un état
                    # parcourir la liste des transitions non déterministes de l'état courant
                    else:
                        # ajouter un nouvel état
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
                        # Exemple: Etat composé de 2 et 1 devient 12
                        new_state = "".join(sorted(new_state))

                        # ajouter le nouvel état si il n'y est pas déjà
                        if new_state not in graph.states:
                            graph.states.append(new_state)

                            # Parcourir les transitions non déterministes
                            # et récupérer les transitions possibles depuis les états d'arrivé
                            for trans in current_node_transitions:
                                goto_nodes = graph.getStateTransitions(
                                    trans.mGoto)
                                # Récupérer les succésseurs des états non déterministes
                                for gtn in goto_nodes:
                                    if gtn in graph_org.transitions:
                                        new_trans = Transition(
                                            new_state, gtn.mValue, gtn.mGoto)
                                        graph.transitions = ajout_trans(
                                            new_trans, graph)
                                # Puis supprimer les transitions non-déterministes
                                graph.transitions.remove(trans)

                            graph.transitions = ajout_trans(
                                Transition(currentTransition, trans.mValue, new_state), graph)
                            states_queue.put(new_state)
                        # Si le nouvel état est déjà dans le graphe
                        # Ajouter que les transitions avec la même logique
                        else:
                            for trans in current_node_transitions:
                                # Parcourir les transitions non déterministes
                                # et récupérer les transitions possibles depuis les états d'arrivé
                                goto_nodes = graph.getStateTransitions(
                                    trans.mGoto)
                                # Puis supprimer les transitions non-déterministes
                                graph.transitions.remove(trans)
                                # Ajouter les nouvelles transitions au graphe
                                new_trans = Transition(
                                    currentTransition, trans.mValue, new_state)
                                graph.transitions = ajout_trans(
                                    new_trans, graph)

            # Etat traité
            state_done.append(currentTransition)

    # Supprimer les états du graphe original non traités
    # Ils n'apparaissent plus dans aucune transition du nouveau graphe déterministe
    print(graph.states)
    print(state_done)
    graph.states = state_done
    graph.transitions = [
        tr for tr in graph.transitions if tr.mFrom in state_done or tr.mGoto in state_done]
    # tmp = graph
    # for state in tmp.states:
    #     if state not in state_done:
    #         print('del: ', state)
    #         graph.states.remove(state)
    #     #     trans = tmp.getStateTransitions(state)
    #     #     for tr in trans:
    #     #         if tr in graph.transitions:
    #     #             graph.transitions.remove(tr)

    # Calcul des états finaux
    # Si un état ajouté contient un des état finaux du graphe initial
    # donc c'est aussi un état final
    for state in graph.states:
        for final in graph.finalStates:
            if final in state:
                graph.finalStates.append(state)
                break
    graph.finalStates = [
        state for state in graph.finalStates if state in state_done]
    # Retourner l'automate déterministe
    return graph
