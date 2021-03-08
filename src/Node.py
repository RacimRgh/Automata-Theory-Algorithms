class Node(object):
    """Node"""

    def __init__(self, value, mFrom, goto):
        self.mFrom = str(value)
        self.mValue = str(mFrom)
        self.mGoto = str(goto)

    def __eq__(self, other):
        return (self.mFrom == other.mFrom) & (self.mValue == other.mValue)
