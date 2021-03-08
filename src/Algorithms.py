class Algorithms(object):
    def __init__(self, graph):
        self.__m_graph = graph

    # Vérifier si un mot appartient au langage
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
                # we always begin at 0
                mot = uInput
                print(mot)
                mot = mot + mot[-1]
                print(mot)
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

    def synchronisation(self):
        print("syncho")

    def determinisation(self):
        print("det")

    def minimisation(self):
        print("min")

    def equivalence(self):
        print("eq")

    def thompson(self):
        print("thomson")
