import csv
from network.graph import NetworkGraph
from faults.injector import FaultInjector
from agents.topology_agent import TopologyAgent


class DatasetGenerator:
    def __init__(self, num_samples=100):
        self.num_samples = num_samples
        self.file_path = "data/dataset.csv"

    def generate(self):
        with open(self.file_path, mode="w", newline="") as file:
            writer = csv.writer(file)

            # Header
            writer.writerow(["fault_edge", "path"])

            for i in range(self.num_samples):
                # Create fresh network
                net = NetworkGraph()
                net.create_sample_network()

                graph = net.get_graph()

                # Inject random fault
                injector = FaultInjector(graph)
                edges = list(graph.edges())

                if not edges:
                    continue

                u, v = edges[i % len(edges)]  # simple variation
                injector.break_link(u, v)

                # Agent finds path
                agent = TopologyAgent(graph)
                path = agent.find_path("A", "D")

                if path:
                    writer.writerow([f"{u}-{v}", path])

        print(f"✅ Dataset generated with {self.num_samples} samples")