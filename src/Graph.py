from src.Node import *


class Graph(object):
    """Clase d'un graphe/automate

    Traite un fichier.txt et retourne l'alphabet, l'état initial, états finaux,
    alphabet, les états et transitions

    Attributes:
        Nodes (list): Liste des transitions de type 'Node'
        finalStates (list): Liste des états finaux (str)
        alphabet (list): L'alphabet du langage
        states (list): Liste des états de l'automate (str)
        initialState (str): Etat initial de l'automate

    """

    def __init__(self, file=None):
        """Constructeur de la classe du graphe

        Le constructeur initialise tout les paramètres du graphe à 
        des valeurs vides, sauf le fichier s'il est donné en paramètre.

        Args:
            file (file): Fichier txt contenant le graphe

        """
        if (file):
            self.file = file
        self.Nodes = []  # transitions
        self.finalStates = []  # états finaux
        self.alphabet = []  # alphabet
        self.states = []  # états
        self.initialState = ''  # état initial

    def parse(self):
        """Fonction de traitement d'un fichier txt

        La fonction lis le fichier txt contenant le graphe
        et génère un objet de type Graph, donc un automate.

        """
        counter = 0
        if self.file != None:
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

    def getStateTransitions(self, state):
        """Récupérer toutes les transitions possibles d'un noeud (state)

        Fonction qui prend un état, et récupère toutes les transitions possible
        depuis ce dernier.

        Args:
            state (str): Etat de départ

        Returns:
            list: Liste des transitions possibles

        """
        transFromState = []
        for node in self.getNodes():
            if (node.mFrom == state):
                transFromState.append(node)

        return transFromState

     # Récupérer toutes les transitions possibles d'un noeud (state) en lisant la lettre (letter)
    def getStateTransitionsLetter(self, state, letter):
        """Récupérer toutes les transitions possibles d'un noeud en lisant une lettre

        Fonction qui prend un état et une lettre de l'alphabet, 
        et récupère toutes les transitions possible en lisant cette lettre
        depuis ce dernier.

        Args:
            state (str): Etat de départ
            letter (str): Lettre de l'alphabet

        Returns:
            list: Liste des transitions possibles

        """
        transFromState = []
        for node in self.getNodes():
            if (node.mFrom == state and node.mValue == letter):
                transFromState.append(node)

        return transFromState

    def nodeToString(self, node):
        """Fonction pour afficher un noeud en chaine de caractère

        Args:
            node (Node): Un noeud (départ, lettre, arrivé)

        Returns:
            str: Le noeud sous forme de chaine de caractères

        """
        return f"Read {node.mValue} from {node.mFrom} to {node.mGoto}"

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
