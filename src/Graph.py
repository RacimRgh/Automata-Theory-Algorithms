class Graph(object):
    """Graph"""

    def __init__(self, value, mFrom, goto):
        self.mFrom = int(value)
        self.mValue = mFrom
        self.mGoto = int(goto)
