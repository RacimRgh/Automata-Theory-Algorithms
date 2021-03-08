from Node import *


class Parser(object):
    """ 
    Traite un fichier.txt et retourne l'alphabet, l'état initial, états finaux,
    alphabet, les états et transitions
    """

    def __init__(self, file):
        self.__m_file = file
        self.__m_Nodes = []  # transitions
        self.__m_finalStates = []  # états finaux
        self.__m_alphabet = []  # alphabet
        self.__m_states = []  # états
        self.__m_initialState = ''  # état initial

    def parse(self):
        counter = 0
        for line in self.__m_file:
            # la première ligne contient les états finaux
            if (counter == 0):
                # les stocker
                self.__m_finalStates = line.rstrip().split(' ')

            # reste du fichier = transitions
            # Premier élément de la première ligne = état initial
            # A chaque ligne ajouter l'état et élément de l'alphabet s'ils n'existent pas déjà
            elif (counter == 1):
                self.__m_initialState = line.rstrip().split(' ')[0]
                line = line.rstrip().split(' ')

                self.__m_states.append(line[0])
                if (line[0] != line[2]):
                    self.__m_states.append(line[2])

                self.__m_Nodes.append(Node(line[0], line[1], line[2]))

                if (line[1] not in self.__m_alphabet):
                    self.__m_alphabet.append(line[1])
            else:
                line = line.rstrip().split(' ')
                if (line[0] not in self.__m_states):
                    self.__m_states.append(line[0])
                if (line[2] not in self.__m_states):
                    self.__m_states.append(line[2])

                self.__m_Nodes.append(Node(line[0], line[1], line[2]))

                if (line[1] not in self.__m_alphabet):
                    self.__m_alphabet.append(line[1])

            counter += 1
        self.close()

    def close(self):
        # Fermer le fichier à la fin
        self.__m_file.close()

    # getters
    def getAlphabet(self):
        return self.__m_alphabet

    def getFinalStates(self):
        return self.__m_finalStates

    def getNodes(self):
        return self.__m_Nodes

    def getStates(self):
        return self.__m_states

    def getInitialState(self):
        return self.__m_initialState
