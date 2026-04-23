import pickle
import pandas as pd


class MLAgent:
    def __init__(self):
        # Load trained model
        with open("models/model.pkl", "rb") as f:
            self.model = pickle.load(f)

        # Load path mapping
        with open("models/path_mapping.pkl", "rb") as f:
            self.mapping = pickle.load(f)

    def predict_path(self, fault_edge):
        # Convert fault_edge → numerical
        node1 = ord(fault_edge.split("-")[0])
        node2 = ord(fault_edge.split("-")[1])

        # Create dataframe (to avoid warning)
        input_df = pd.DataFrame([[node1, node2]], columns=["node1", "node2"])

        # Predict label
        label = self.model.predict(input_df)[0]

        # Convert label → actual path
        return self.mapping[label]