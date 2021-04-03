from src.Node import Node
from src.Graph import Graph


def acceptation(graph, words):
    """Fonction de vérification d'acceptation de mots par un automate

    Algorithme prenant un automate déterministe et un mot, et décidant si
    le mot est accepté par l'automate.

    Args:
        graph (Graph): Un automate sous forme d'objet de la classe Graph
        words (list): Liste de mots à vérifier

    Returns:
        dic: Dictionnaire ayant pour clés les mots donnés en paramètre, et
        comme valeur un booléen selon si il est accepté ou non.
    """
    nodes = graph.getNodes()
    finalStates = graph.getFinalStates()
    alphabet = graph.getAlphabet()
    initialState = graph.getInitialState()
    result = {}
    for word in words:
        result[word] = False
    # print(initialState)
    # get string to check against
    for uInput in words:
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
