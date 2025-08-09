import random

# run simulations for movement modes and collect results
def run_simulation(graph, agent, num_episodes=1000):
    random_walk_results = []
    shortest_path_results = []

    # initialize visit counters for each node
    random_walk_visits = {node_name: 0 for node_name in graph.nodes}
    shortest_path_visits = {node_name: 0 for node_name in graph.nodes}

    node_names = list(graph.nodes.keys())

    for _ in range(num_episodes):
        start_name, target_name  = random.sample(node_names,2)
        start_node = graph.nodes[start_name]
        target_node = graph.nodes[target_name]

        # random walk simulation
        agent.random_walk(start_node, target_node)
        random_walk_results.append({
            "start": start_name,
            "target": target_name,
            "visited_nodes": [node.name for node in agent.memory]
        })

        # visit counts
        for node in agent.memory:
            random_walk_visits[node.name] += 1

        # shortest path simulation
        agent.shortest_path_walk(start_node, target_node)
        shortest_path_results.append({
            "start": start_name,
            "target": target_name,
            "visited_nodes": [node.name for node in agent.memory]
        })

        # visit counts
        for node in agent.memory:
            shortest_path_visits[node.name] += 1

    return random_walk_results, shortest_path_results, random_walk_visits, shortest_path_visits
