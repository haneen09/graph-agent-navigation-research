from World_design import Graph

class GraphMetrics:
    def __init__(self, graph):
        self.graph = graph

    # calculate degree centrality for each node
    def degree_centrality(self):
        return {node.name: len(node.neighbors) for node in self.graph.nodes.values()}

    # calculate closeness centrality for each node
    def closeness_centrality(self):
        centrality = {}
        for node in self.graph.nodes.values():
            total_distance = 0
            for other_node in self.graph.nodes.values():
                if node != other_node:
                    path_length = self.shortest_path_length(node, other_node)
                    total_distance += path_length
            if total_distance > 0:
                centrality[node.name] = (len(self.graph.nodes) - 1) / total_distance
            else:
                centrality[node.name] = 0
        return centrality

    # calculates betweenness centrality of each node
    def betweenness_centrality(self):
        centrality = {node.name: 0 for node in self.graph.nodes.values()}
        for start in self.graph.nodes.values():
            for end in self.graph.nodes.values():
                if start != end:
                    # get all shortest paths from start to end
                    paths = self.all_shortest_paths(start, end)
                    num_paths = len(paths)
                    if num_paths > 0:
                        for path in paths:
                            for node in path:
                                if node != start and node != end:
                                    centrality[node.name] += 1 / num_paths  # increment by the fraction of paths
        return centrality

    # shortest path length between two nodes using breadth-first search (BFS)
    def shortest_path_length(self, start_node, end_node):
        visited = {start_node: 0}
        queue = [start_node]
        while queue:
            current = queue.pop(0)
            if current == end_node:
                return visited[current]
            for neighbor in current.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = visited[current] + 1
                    queue.append(neighbor)
        return float('inf')

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

# create the graph and add edges
graph = Graph()
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("C", "D")
graph.add_edge("C", "E")
graph.add_edge("D", "F")
graph.add_edge("E", "F")

graph.display_graph()

start_node = graph.nodes["A"]
end_node = graph.nodes["F"]
paths = graph.all_shortest_paths(start_node, end_node)

for path in paths:
    print(" --> ".join(node.name for node in path))

graph_metrics = GraphMetrics(graph)
degree_centrality = graph_metrics.degree_centrality()
closeness_centrality = graph_metrics.closeness_centrality()
betweenness_centrality = graph_metrics.betweenness_centrality()

print("Degree centrality: ", {k: round(v, 2) for k, v in degree_centrality.items()})
print("Closeness centrality: ", {k: round(v, 2) for k, v in closeness_centrality.items()})
print("Betweenness centrality: ", {k: round(v, 2) for k, v in betweenness_centrality.items()})