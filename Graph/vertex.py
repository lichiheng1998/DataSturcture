from Graph import _WHITE, _GREY, _BLACK

class Vertex:
    def __init__(self, label):
        self.label = label
        self.color = _WHITE
        self.d = -1
        self.f = -1
        self.parent = None

    def __hash__(self):
        return hash(self.label)

    def __eq__(self, other):
        return self.label == other.label

    def __str__(self):
        par = "None" if self.parent is None else str(self.parent.label)
        return "label: " + str(self.label) + ", d: " + str(self.d) + ", f: " + str(self.f) + ", parent: " + par
