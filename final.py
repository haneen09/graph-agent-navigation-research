import random
from World_design import Graph
from World_metrics import GraphMetrics, graph
from Agent import Agent
from simulation import run_simulation

# precomputing the shortest paths between all pairs of nodes in the graph
def precompute_shortest_paths(graph):
    shortest_paths = {}
    for start_name in graph.nodes:
        for end_name in graph.nodes:
            if start_name != end_name:
                start_node = graph.nodes[start_name]
                end_node = graph.nodes[end_name]
                paths = graph.all_shortest_paths(start_node, end_node)
                if paths:
                    shortest_paths[(start_node, end_node)] = paths[0]

    return shortest_paths

# Create the graph and add edges
graph = Graph()
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("C", "D")
graph.add_edge("C", "E")
graph.add_edge("D", "F")
graph.add_edge("E", "F")


# Precompute shortest paths
shortest_paths = precompute_shortest_paths(graph)

# Initialize agent
agent = Agent(graph, shortest_paths)


# run simulation
num_episodes = 1000
(random_walk_data, shortest_path_data, random_walk_visits,
 shortest_path_visits) = run_simulation(graph, agent, num_episodes)

graph_metrics = GraphMetrics(graph)
degree_centrality = graph_metrics.degree_centrality()
closeness_centrality = graph_metrics.closeness_centrality()
betweenness_centrality = graph_metrics.betweenness_centrality()

# simulation data test
print("Random Walk Data (First 10 episodes):", random_walk_data[:10])
print("Shortest Path Data (First 10 episodes):", shortest_path_data[:10])