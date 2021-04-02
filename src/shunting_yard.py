##################

def prefix_regex(exp):
    prio = {
        ')': 0,
        '(': 0,
        '*': 3,
        '.': 1,
        '+': 1,
        '?': 1
    }
    operators = ['*', '.', '+']
    # op_stack = deque()
    # out_stack = deque()
    op_stack = []
    out_stack = []
    print("thomson")
    for c in exp:
        # Si le caractère lu n'est ni opérateur ni ( )
        # L'ajoute à la pile de sortie
        if c not in prio.keys():
            # print('1-', c)
            out_stack.append(c)

        # Si le caractère est un opérateur
        elif c in operators:
            # print('2-', c)
            # 1 - Si le sommet est un opérateur avec une + grande priorité
            if len(op_stack) > 0:
                top = op_stack.pop()
                while top in operators and prio[top] >= prio[c]:
                    out_stack.append(top)
                    # Parcours la pile tant que le sommet est un opérateur
                    # et est plus prioritaire que la caractère lu
                    # while (len(op_stack) > 0):
                    if (len(op_stack) == 0):
                        break
                    top = op_stack.pop()
                    if (top in operators and prio[top] < prio[c]) or top not in operators:
                        break
                    # out_stack.append(top)
                # Si le caractère lu est un opérateur, et le sommet de pile est une '('
                if top in operators and prio[top] < prio[c]:
                    op_stack.append(top)
                    op_stack.append(c)
                if top == '(':
                    op_stack.append(top)
                    op_stack.append(c)
                if (len(op_stack) == 0):
                    op_stack.append(c)
            else:
                op_stack.append(c)

        # Si le caractère lu est une '('
        elif c == '(':
            # print('3-', c)
            op_stack.append(c)

        # Si le caractère lu == ')': dépiler tout les opérateurs jusqu'à arriver à '('
        elif c == ')':
            # print('4-', c)
            if (len(op_stack) > 0):
                top = op_stack.pop()
                if top in operators:
                    out_stack.append(top)
                    while (len(op_stack) > 0):
                        top = op_stack.pop()
                        if top == '(':
                            break
                        out_stack.append(top)
                else:
                    print('Mauvaise expression.')
    for op in op_stack:
        out_stack.append(op)
    return out_stack
