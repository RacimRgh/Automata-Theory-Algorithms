from Node import Node
from Parser import Parser


def synchronisation(graph):
    """Algorithme de suppresion des epsilon transitions

    Algorithme calculant un automate équivalent au premier, sans "epsilon-transitions".

    """
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
