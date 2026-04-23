import networkx as nx


class TopologyAgent:
    def __init__(self, graph):
        self.graph = graph

    def get_active_graph(self):
        """
        Create a filtered graph that only includes working (status='up') edges
        """
        active_graph = nx.Graph()

        for u, v, data in self.graph.edges(data=True):
            if data["status"] == "up":
                active_graph.add_edge(u, v, weight=data["weight"])

        return active_graph

    def find_path(self, source, target):
        """
        Find the shortest path between source and target
        using only active (working) edges
        """
        active_graph = self.get_active_graph()

        try:
            path = nx.shortest_path(active_graph, source, target, weight="weight")
            return path
        except nx.NetworkXNoPath:
            return None

    def apply_fix(self, path):
        """
        Apply fix by ensuring all edges in the chosen path are active (status='up')
        """
        if not path:
            print("❌ No path to fix network")
            return

        print("\n🛠 Applying fix using path:", path)

        for i in range(len(path) - 1):
            u = path[i]
            v = path[i + 1]

            if self.graph.has_edge(u, v):
                self.graph[u][v]["status"] = "up"