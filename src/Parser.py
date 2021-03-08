from Node import *


class Parser(object):
    """ 
    Traite un fichier.txt et retourne l'alphabet, l'état initial, états finaux,
    alphabet, les états et transitions
    """

    def __init__(self, file=None):
        if (file):
            self.file = file
        self.Nodes = []  # transitions
        self.finalStates = []  # états finaux
        self.alphabet = []  # alphabet
        self.states = []  # états
        self.initialState = ''  # état initial

    def parse(self):
        counter = 0
        for line in self.file:
            # la première ligne contient les états finaux
            if (counter == 0):
                # les stocker
                self.finalStates = line.rstrip().split(' ')

            # reste du fichier = transitions
            # Premier élément de la première ligne = état initial
            # A chaque ligne ajouter l'état et élément de l'alphabet s'ils n'existent pas déjà
            elif (counter == 1):
                self.initialState = line.rstrip().split(' ')[0]
                line = line.rstrip().split(' ')

                self.states.append(line[0])
                if (line[0] != line[2]):
                    self.states.append(line[2])

                self.Nodes.append(Node(line[0], line[1], line[2]))

                if (line[1] not in self.alphabet):
                    self.alphabet.append(line[1])
            else:
                line = line.rstrip().split(' ')
                if (line[0] not in self.states):
                    self.states.append(line[0])
                if (line[2] not in self.states):
                    self.states.append(line[2])

                self.Nodes.append(Node(line[0], line[1], line[2]))

                if (line[1] not in self.alphabet):
                    self.alphabet.append(line[1])

            counter += 1
        self.close()

    def close(self):
        # Fermer le fichier à la fin
        self.file.close()

    # getters
    def getAlphabet(self):
        return self.alphabet

    def getFinalStates(self):
        return self.finalStates

    def getNodes(self):
        return self.Nodes

    def getStates(self):
        return self.states

    def getInitialState(self):
        return self.initialState

    # Récupérer toutes les transitions possibles d'un noeud (state)
    def getStateTransitions(self, state):
        transFromState = []
        for node in self.getNodes():
            if (node.mFrom == state):
                transFromState.append(node)

        return transFromState

    def nodeToString(self, node):
        return f"Read {node.mValue} from {node.mFrom} to {node.mGoto}"

    # setters
    def setAlphabet(self, alphabet):
        self.alphabet = alphabet

    def setFinalStates(self, final_states):
        self.finalStates = final_states

    def setNodes(self, nodes):
        self.Nodes = nodes

    def setStates(self, states):
        self.states = states

    def setInitialState(self, initialState):
        self.initialState = initialState
