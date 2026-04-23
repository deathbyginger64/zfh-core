import random


class FaultInjector:
    def __init__(self, graph):
        self.graph = graph

    def break_link(self, u, v):
        if self.graph.has_edge(u, v):
            self.graph[u][v]["status"] = "down"
            print(f"⚠️ Link {u}-{v} is now DOWN")
        else:
            print("❌ Edge does not exist")

    def break_random_link(self):
        edges = list(self.graph.edges())

        if not edges:
            print("❌ No edges to break")
            return

        u, v = random.choice(edges)

        self.graph[u][v]["status"] = "down"
        print(f"⚠️ Random Fault: Link {u}-{v} is now DOWN")