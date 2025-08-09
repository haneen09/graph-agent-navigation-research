# represents a node in the graph
class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = []  # stores connected nodes

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def __repr__(self):
        return f"Node({self.name})"


# represents an edge between two nodes
class Edge:
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2

    def __repr__(self):
        return f"Edge({self.node1.name} - {self.node2.name})"


# graph structure with nodes and edges
class Graph:
    def __init__(self):
        self.nodes = {}  # dictionary to store nodes by name
        self.edges = []  # list to store edges

    def add_node(self, name):
        if name not in self.nodes:
            self.nodes[name] = Node(name)
        return self.nodes[name]

    def add_edge(self, name1, name2):
        node1 = self.add_node(name1)
        node2 = self.add_node(name2)
        node1.add_neighbor(node2)
        node2.add_neighbor(node1)
        self.edges.append(Edge(node1, node2))

    def display_graph(self):
        for node in self.nodes.values():
            print(f"{node.name}: {[n.name for n in node.neighbors]}")  # show connections


# all shortest paths between two nodes
    def all_shortest_paths(self, start_node, end_node):
        paths = []
        queue = [(start_node, [start_node])]
        while queue:
            current, path = queue.pop(0)
            if current == end_node:
                paths.append(path)
            else:
                for neighbor in current.neighbors:
                    if neighbor not in path:
                        new_path = path + [neighbor]
                        queue.append((neighbor, new_path))
        return paths



