from src.Transition import Transition
from src.Graph import Graph


def clean_graph(graph):
    i = 0
    while i < len(graph.states):
        delete = False
        sources = []
        destinations = []
        # Les destinations de l'état courant, sans compter les boucles
        destinations = [
            node.mGoto for node in graph.transitions if node.mFrom == graph.states[i] and node.mGoto != graph.states[i]]
        # Les états qui vont vers l'état courant sans compter les boucles
        sources = [
            node.mFrom for node in graph.transitions if node.mGoto == graph.states[i] and node.mFrom != graph.states[i]]

        # Etat initial sans succéssseur à part lui même
        if (graph.states[i] == graph.initialState):
            if (len(destinations) == 0):
                delete = True

        # Etat final sans prédécesseur à part lui même
        if (graph.states[i] in graph.finalStates):
            if (len(sources) == 0):
                delete = True

        # Etat sans successeur à part lui même et pas final
        if (len(destinations) == 0 and graph.states[i] not in graph.finalStates):
            delete = True

        # Etat isolé
        if (len(destinations) == 0 and len(sources) == 0):
            delete = True

        # Etat source, sans noeud qui y va, et n'est pas initial = inaccessible
        if (len(sources) == 0 and graph.states[i] != graph.initialState):
            delete = True

        if delete == True:
            graph.transitions = [
                tr for tr in graph.transitions if tr.mFrom != graph.states[i] and tr.mGoto != graph.states[i]]
            if graph.states[i] in graph.finalStates:
                graph.finalStates.remove(graph.states[i])
            graph.states.remove(graph.states[i])
            i = 0
        else:
            i = i + 1

    return graph


def synchronisation(graph):
    """Algorithme de suppresion des epsilon transitions

    Algorithme calculant un automate équivalent au premier, sans "epsilon-transitions".

    """
    print("syncho")
    nodes = graph.gettransitions()
    # alphabet = graph.getAlphabet()
    # for node in nodes:
    i = 0
    while i < len(nodes):
        if nodes[i].mValue == "\u03b5":
            epsilonTransitions = graph.getStateTransitions(
                nodes[i].mGoto)
            for trans in epsilonTransitions:
                print(graph.nodeToString(trans))
                nodes.append(
                    Transition(nodes[i].mFrom, trans.mValue, trans.mGoto))
                # algorithme calculant un automate déterministe équivalent au premier.
            nodes.remove(nodes[i])
            i = 0
        i = i + 1

    graph = clean_graph(graph)

    return graph
