import pickle
import pandas as pd


class MLAgent:
    def __init__(self):
        with open("models/model.pkl", "rb") as f:
            self.model = pickle.load(f)

        with open("models/path_mapping.pkl", "rb") as f:
            self.mapping = pickle.load(f)

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
                weights.append(0)

        return weights

    def predict_path(self, fault_edge, num_active_links, graph):
        node1 = ord(fault_edge.split("-")[0])
        node2 = ord(fault_edge.split("-")[1])

        weights = self.get_weight_features(graph)

        data = [[node1, node2, num_active_links] + weights]

        columns = ["node1", "node2", "num_active_links"]
        columns += [f"{u}-{v}_weight" for u, v in self.edge_order]

        input_df = pd.DataFrame(data, columns=columns)

        label = self.model.predict(input_df)[0]

        return self.mapping[label]