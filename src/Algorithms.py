from Node import *


class Algorithms(object):
    def __init__(self, graph):
        self.__m_graph = graph

    # algorithme prenant un automate déterministe et un mot, et décidant si le mot est accepté par l'automate.
    def acceptation(self):
        # parse file and store states
        nodes = self.__m_graph.getNodes()
        finalStates = self.__m_graph.getFinalStates()
        alphabet = self.__m_graph.getAlphabet()
        initialState = self.__m_graph.getInitialState()
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

    # algorithme calculant un automate équivalent au premier, sans "epsilon-transitions.
    def synchronisation(self):
        print("syncho")
        nodes = self.__m_graph.getNodes()
        # alphabet = self.__m_graph.getAlphabet()
        for node in nodes:
            if node.mValue == "\u03b5":
                epsilonTransitions = self.__m_graph.getStateTransitions(
                    node.mGoto)
                for epsilonNode in epsilonTransitions:
                    print(self.__m_graph.nodeToString(epsilonNode))
                    nodes.append(
                        Node(node.mFrom, epsilonNode.mValue, epsilonNode.mGoto))
                    # algorithme calculant un automate déterministe équivalent au premier.
                nodes.remove(node)
        return self.__m_graph

    def determinisation(self):
        print("det")

    # algorithme calculant un automate déterministe minimal équivalent au premier.
    def minimisation(self):
        print("min")

    # algorithme prenant deux automates, et déterminant si ceux-ci sont équivalents.
    def equivalence(self):
        print("eq")

    # algorithme prenant une expression régulière, et retournant l'automate de Thompson calculant le langage correspondant à cette expression.
    def thompson(self):
        print("thomson")
