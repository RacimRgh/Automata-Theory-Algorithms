class Node(object):
    """Node"""

    def __init__(self, value, mFrom, goto):
        self.mFrom = str(value)
        self.mValue = str(mFrom)
        self.mGoto = str(goto)
