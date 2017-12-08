class Node:
    def __init__(self, _name, _weight=None):
        self.name = _name
        self.weight = _weight
        self.parent = None
        self.children = None

    def __str__(self):
        return "node {} ({}) with parent {}".format( \
            self.name, self.weight, self.parent)
