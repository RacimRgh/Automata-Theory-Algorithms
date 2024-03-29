from src.shunting_yard import prefix_regex
from src.Graph import Graph
from src.Transition import Transition


def gen_state(states):
    for i in range(100):
        if str(i) not in states:
            return str(i)


def thompson(exp):
    """Fonction de transformation d'une expression postfixé en automate

    Algorithme prenant une expression régulière, et retournant l'automate de Thompson calculant le langage correspondant à cette expression.

    """
    out_stack = prefix_regex(exp)
    print(out_stack)
    graph_stack = []
    thompson_graph = Graph()
    operators = ['*', '.', '+']
    states = []
    for c in out_stack:
        # Si c'est un caractère
        # Créer un graphe avec un etat initial et etat final, et transition en lisant c
        if c not in operators:
            print("1-", c)
            g = Graph()
            print(len(graph_stack))

            g.alphabet.append(c)  # ajouter la lettre à l'alphabet

            i = gen_state(states)  # générer l'état initial
            states.append(i)
            g.initialState = i
            g.states.append(i)

            j = gen_state(states)  # générer l'état final
            states.append(j)
            g.finalStates.append(j)
            g.states.append(j)

            # ajouter la transition (initial, c, final)
            g.transitions.append(Transition(i, c, j))
            # ajouter le graphe à la pile
            graph_stack.append(g)
        # Si
        elif c == '*':
            print("2-", c)
            g = Graph()
            g = graph_stack.pop()  # récupérer le dernier graphe dans la pile
            print(len(graph_stack))

            g.transitions.append(
                Transition(g.finalStates[0], '\u03b5', g.initialState))

            i = gen_state(states)  # générer l'état initial
            g.states.append(i)
            states.append(i)
            g.transitions.append(Transition(i, '\u03b5', g.initialState))
            g.initialState = i

            j = gen_state(states)  # générer l'état final
            g.states.append(j)
            states.append(j)
            g.transitions.append(Transition(g.finalStates[0], '\u03b5', j))
            g.finalStates = []
            g.finalStates.append(j)
            g.transitions.append(
                Transition(g.initialState, '\u03b5', g.finalStates[0]))

            graph_stack.append(g)
        # Si
        elif c == '+':
            print("3-", c)
            print(len(graph_stack))
            g1 = graph_stack.pop()
            g2 = graph_stack.pop()
            g = Graph()

            g.states = list(set().union(g1.states, g2.states))
            # g.states = [state for state in g1.states if state not in g.states]
            # g.states = [state for state in g2.states if state not in g.states]
            g.alphabet = list(set().union(g1.alphabet, g2.alphabet))
            # g.alphabet = [c for c in g1.alphabet if c not in g.alphabet]
            # g.alphabet = [c for c in g2.alphabet if c not in g.alphabet]
            for node in g1.transitions:
                g.transitions.append(node)
            for node in g2.transitions:
                g.transitions.append(node)

            i = gen_state(states)  # générer l'état initial
            g.states.append(i)
            states.append(i)
            g.transitions.append(Transition(i, '\u03b5', g1.initialState))
            g.transitions.append(Transition(i, '\u03b5', g2.initialState))
            g.initialState = i

            j = gen_state(states)  # générer l'état final
            g.states.append(j)
            states.append(j)
            g.transitions.append(Transition(g1.finalStates[0], '\u03b5', j))
            g.transitions.append(Transition(g2.finalStates[0], '\u03b5', j))
            g.finalStates = []
            g.finalStates.append(j)

            graph_stack.append(g)
        # si
        elif c == '.':
            print("4-", c)
            print(len(graph_stack))
            g1 = graph_stack.pop()
            g2 = graph_stack.pop()
            g = Graph()

            g.transitions = [node for node in g2.transitions]
            g.alphabet = list(set().union(g1.alphabet, g2.alphabet))
            g.states = [
                state for state in g1.states if state not in g.states and state != g1.initialState]
            g.states = list(set().union(g.states, g2.states))

            g.initialState = g2.initialState
            g.finalStates.append(g1.finalStates[0])

            for node in g1.transitions:
                if node.mFrom != g1.initialState:
                    g.transitions.append(node)
                else:
                    g.transitions.append(
                        Transition(g2.finalStates[0], node.mValue, node.mGoto))
            graph_stack.append(g)

    thompson_graph = graph_stack.pop()
    return thompson_graph
