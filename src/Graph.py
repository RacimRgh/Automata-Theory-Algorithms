class Graph(object):
    """Graph"""

    def __init__(self, value, mFrom, goto):
        self.mValue = int(value)
        self.mFrom = mFrom
        self.mGoto = int(goto)
