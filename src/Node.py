class Node(object):
    """Node: Un noeud

    Un noeud représente un état de départ, une lettre de l'alphabet
    à lire et un état d'arriver

    """

    def __init__(self, value, mFrom, goto):
        self.mFrom = str(value)
        self.mValue = str(mFrom)
        self.mGoto = str(goto)

    def __eq__(self, other):
        """Fonction d'égalité

        Redéfinition de la fonction d'égalité pour comparer les attributs
        du noeud et non pas l'objet en entier.

        """
        return (self.mFrom == other.mFrom) & (self.mValue == other.mValue) & (self.mGoto == other.mGoto)
