from src.Transition import Transition
from src.Algorithms.minimisation import minimisation
from src.Graph import Graph


def equivalence(graph1, graph2):
    """ Fonction de vérification de l'équivalence de deux automates

    Algorithme prenant deux automates, et déterminant si ceux-ci sont équivalents.

    """
    # graph1_min = minimisation(graph1)
    # graph2_min = minimisation(graph2)
    graph1_min = graph1
    graph2_min = graph2

    print("eq")
    if len(graph1_min.states) != len(graph2_min.states):
        print('Nombre d\'états différent')
        return False

    graph1_min.alphabet.sort()
    graph2_min.alphabet.sort()
    if graph1_min.alphabet != graph2_min.alphabet:
        print('Alphabets différents')
        return False

    queue1 = [graph1_min.initialState]
    queue2 = [graph2_min.initialState]
    done1 = []
    done2 = []
    type1 = {}
    type2 = {}
    while (len(queue1) > 0 and len(queue2) > 0):
        current1 = queue1.pop()
        current2 = queue2.pop()
        for letter in graph1_min.alphabet:
            trans1 = graph1_min.getStateTransitionsLetter(current1, letter)
            trans2 = graph2_min.getStateTransitionsLetter(current2, letter)
            if len(trans1) != len(trans2):
                print('Transitions différentes')
                return False
            elif len(trans1) != 0 and len(trans2) != 0:
                dest1 = trans1[0].mGoto
                dest2 = trans2[0].mGoto

                # Vérifier le type de l'état destination du premier automate
                if dest1 == graph1_min.initialState and dest1 in graph1_min.finalStates:
                    type1[dest1] = 'initial and final'
                elif dest1 == graph1_min.initialState:
                    type1[dest1] = 'initial'
                elif dest1 in graph1_min.finalStates:
                    type1[dest1] = 'final'
                else:
                    type1[dest1] = 'other'

                # Vérifier le type de l'état destination du deuxième automate
                if dest2 == graph2_min.initialState and dest2 in graph2_min.finalStates:
                    type2[dest2] = 'initial and final'
                elif dest2 == graph2_min.initialState:
                    type2[dest2] = 'initial'
                elif dest2 in graph2_min.finalStates:
                    type2[dest2] = 'final'
                else:
                    type2[dest2] = 'other'

                # Si les états sont de nature différente alors les automates ne sont pas équivalents
                if type1[dest1] != type2[dest2]:
                    return False

                done1.append(current1)
                if dest1 not in done1:
                    queue1.append(dest1)

                done2.append(current2)
                if dest2 not in done2:
                    queue2.append(dest2)
    print('Les graphes sont équivalents!')
    return True
