"""Module de génération automatique d'automates

Todo:
    * Ajouter des cas de noeuds non valides

"""


from src.Transition import *
from src.Graph import *
import random
from random import seed
from random import choice
from string import ascii_lowercase
import os


def valid_node(g):
    """Fonction de vérification de noeuds générés

    La fonction vérifie si le graphe généré contient des noeuds 'inutiles'
    qui le rendent non pertinent

    Example:
        * Etat isolé
        * Etat initial sans transition sortante
        * Etat final sans transition entrante
        * Etat puit 

    Args:
        g (Graph): Un graphe généré automatiquement

    Returns:
        boolean: true si graphe pertinent, false sinon

    """
    for state in g.states:
        sources = []
        destinations = []
        # Les destinations de l'état courant, sans compter les boucles
        destinations = [
            node.mGoto for node in g.transitions if node.mFrom == state and node.mGoto != state]
        # Les états qui vont vers l'état courant sans compter les boucles
        sources = [
            node.mFrom for node in g.transitions if node.mGoto == state and node.mFrom != state]

        # Etat initial sans succéssseur à part lui même
        if (state == g.initialState):
            if (len(destinations) == 0):
                return False

        # Etat final sans prédécesseur à part lui même
        if (state in g.finalStates):
            if (len(sources) == 0):
                return False

        # Etat sans successeur à part lui même et pas final
        if (len(destinations) == 0 and state not in g.finalStates):
            return False

        # Etat isolé
        if (len(destinations) == 0 and len(sources) == 0):
            return False

        # Etat source, sans noeud qui y va, et n'est pas initial = inaccessible
        if (len(sources) == 0 and state != g.initialState):
            return False

    return True


def generate_lang():
    """Fonction de génération automatique d'automates

    En utilisant la librarie random, générer des états et alphabets
    pour ensuite créer toutes les combinaisons de transitions 
    possibles. A la fin on réduit le nombre de transitions à un 
    nombre réaliste, et on vérifie si le graphe est pertinent avec
    la fonction précédente

    Returns:
        graphe: Graphe de la classe Graph

    """
    repeat = False
    while repeat == False:

        n_states = random.randint(4, 7)
        n_alphabet = random.randint(2, 3)
        n_finaux = random.randint(1, 3)
        n_nodes = random.randint(7, 10)
        graph = Graph()

        # Générer les lettres de l'alphabet
        for i in range(n_alphabet):
            graph.alphabet.append(ascii_lowercase[i])

        # Générer les états et les noeuds de l'automate
        for i in range(n_states):
            graph.states.append(str(i+1))
            for x in graph.alphabet:
                for j in range(n_states+1):
                    graph.transitions.append(Transition(str(i), x, str(j)))

        # Choisir les états finaux de l'automate
        for i in range(n_finaux):
            select_fin = choice(graph.states)
            if select_fin not in graph.finalStates:
                graph.finalStates.append(select_fin)

        graph.initialState = choice(graph.states)

        while(len(graph.transitions) > n_nodes):
            select_del = choice(graph.transitions)
            graph.transitions.remove(select_del)

        repeat = valid_node(graph)
    return graph
