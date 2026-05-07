import csv
import random
from network.graph import NetworkGraph
from faults.injector import FaultInjector
from agents.topology_agent import TopologyAgent


class DatasetGenerator:
    def __init__(self, num_samples=500):
        self.num_samples = num_samples
        self.file_path = "data/dataset.csv"

        # Fixed edge order (VERY IMPORTANT)
        self.edge_order = [
            ("A", "B"),
            ("A", "E"),
            ("B", "C"),
            ("B", "E"),
            ("C", "D"),
            ("D", "E")
        ]

    def get_weight_features(self, graph):
        weights = []

        for u, v in self.edge_order:
            if graph.has_edge(u, v):
                weights.append(graph[u][v]["weight"])
            else:
                weights.append(0)  # if edge missing

        return weights

    def generate(self):
        with open(self.file_path, mode="w", newline="") as file:
            writer = csv.writer(file)

            # Header
            header = ["fault_edge", "num_active_links"]
            header += [f"{u}-{v}_weight" for u, v in self.edge_order]
            header += ["path"]

            writer.writerow(header)

            for i in range(self.num_samples):
                print(f"\n--- Sample {i+1} ---")

                net = NetworkGraph()
                net.create_sample_network()
                graph = net.get_graph()

                edges = list(graph.edges())
                if not edges:
                    continue

                # Random fault
                u, v = random.choice(edges)
                injector = FaultInjector(graph)
                injector.break_link(u, v)

                fault_edge = f"{u}-{v}"

                # Active links
                active_links = sum(
                    1 for (x, y) in graph.edges()
                    if graph[x][y]["status"] == "up"
                )

                # Weight features
                weights = self.get_weight_features(graph)

                # Correct path
                agent = TopologyAgent(graph)
                path = agent.find_path("A", "D")

                if path:
                    row = [fault_edge, active_links] + weights + [path]
                    writer.writerow(row)

        print(f"\n✅ Dataset generated with {self.num_samples} samples")