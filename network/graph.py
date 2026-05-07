import networkx as nx
import random


class NetworkGraph:
    def __init__(self):
        self.graph = nx.Graph()

    def create_sample_network(self):
        # Nodes
        nodes = ["A", "B", "C", "D", "E"]
        self.graph.add_nodes_from(nodes)

        # Base edges
        possible_edges = [
            ("A", "B"),
            ("A", "E"),
            ("B", "C"),
            ("B", "E"),
            ("C", "D"),
            ("D", "E")
        ]

        # 🔥 Randomly choose edges (simulate topology variation)
        selected_edges = random.sample(possible_edges, k=len(possible_edges))

        for u, v in selected_edges:
            weight = random.randint(1, 10)  # 🔥 random weight
            self.graph.add_edge(u, v, weight=weight, status="up")

    def get_graph(self):
        return self.graph

    def display(self):
        print("\n📡 Network Connections:")
        for u, v, data in self.graph.edges(data=True):
            print(f"{u} ↔ {v} | weight={data['weight']} | status={data['status']}")