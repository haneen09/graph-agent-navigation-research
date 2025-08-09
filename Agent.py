import random

class Agent:
    def __init__(self, graph, shortest_paths):
        self.graph = graph
        self.shortest_paths = shortest_paths
        self.memory = []

# creating a random walk from start_node to target_node
    def random_walk(self, start_node, target_node):
        current_node = start_node
        self.memory = [current_node]

        while current_node != target_node:
            neighbors = current_node.neighbors
            current_node = random.choice(neighbors)
            self.memory.append(current_node)

        return self.memory

# creating a walk using the precomputed shortest path
    def shortest_path_walk(self, start_node, target_node):
        self.memory = self.shortest_paths[(start_node, target_node)]
        return self.memory

# return the agent's current state with the visited nodes memory
    def sense_state(self):
        return{
            "start ": self.memory[0],
            "target ": self.memory[-1],
            "visited_nodes ": [node.name for node in self.memory]
        }