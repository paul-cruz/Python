class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = list()
        self.distance = 9999
        self.visited = False

    def add_neighbor(self, vert):
        if vert not in self.neighbors:
            self.neighbors.append(vert)
            self.neighbors.sort()
