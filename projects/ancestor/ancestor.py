
from util import Stack, Queue


class Graph:

    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):

        if vertex not in self.vertices:
            self.vertices[vertex] = set()


    def add_edge(self, v1, v2):

        if v1 and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("that vertex does not exist")


def earliest_ancestor(ancestors, starting_node):

    graph = Graph()

    for i in ancestors:
        graph.add_vertex(i[0])
        graph.add_vertex(i[1])

        graph.add_edge(i[1],i[0])

    q = Queue()

    visited = set()

    longest_path = 1
    parent_end = -1

    q.enqueue([starting_node])

    while q.size() > 0:

        path = q.dequeue()

        vertex = path[-1]

        if len(path) >= longest_path and vertex < parent_end or len(path) > longest_path:
            parent_end = vertex
            visited.add(vertex)



        for neighbor in graph.vertices[vertex]:
                path_add = path.copy()
                path_add.append(neighbor)
                q.enqueue(path_add)

    return parent_end