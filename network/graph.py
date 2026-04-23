import networkx as nx


class NetworkGraph: # constructor
    def __init__(self):
        self.graph = nx.Graph()  # creates an empty network 

    def create_sample_network(self):
        edges = [
            ("A", "B", 5),
            ("B", "C", 1),
            ("C", "D", 1),
            ("A", "E", 2),
            ("E", "D", 2),
            ("B", "E", 2)
        ]

        for u, v, w in edges:  # defines a connection , u = start , v = end , w = weight , status = up means the following edge is working 
            self.graph.add_edge(u, v, weight=w, status="up")

    def get_graph(self):
        return self.graph

    def display(self):
        print("\n📡 Network Connections:")
        for u, v, data in self.graph.edges(data=True):
            print(f"{u} ↔ {v} | weight={data['weight']} | status={data['status']}")