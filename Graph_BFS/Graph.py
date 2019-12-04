from Vertex import Vertex

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, source, destination):
        if source in self.vertices and destination in self.vertices:
            for key, value in self.vertices.items():
                if key == source:
                    value.add_neighbor(destination)
                if key == destination:
                    value.add_neighbor(source)
            return True
        else:
            return False
    
    def print_graph(self):
        for key in self.vertices:
            print(key + str(self.vertices[key].neighbors) + " " + str(self.vertices[key].distance))
    
    def bfs(self, vert):
        q = list()
        vert.distance = 0
        vert.visited = True

        for v in vert.neighbors:
            self.vertices[v].distance = vert.distance + 1
            q.append(v)

        while len(q) > 0:
            u = q.pop(0)
            node_u = self.vertices[u]
            node_u.visited = True

            for v in node_u.neighbors:
                node_v = self.vertices[v]
                if not node_v.visited:
                    q.append(v)
                    if node_v.distance > node_u.distance +1:
                        node_v.distance = node_u.distance + 1