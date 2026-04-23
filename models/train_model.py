import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle


class ModelTrainer:
    def __init__(self):
        self.data_path = "data/dataset.csv"
        self.model_path = "models/model.pkl"
        self.mapping_path = "models/path_mapping.pkl"

    def preprocess(self, df):
        df["node1"] = df["fault_edge"].apply(lambda x: ord(x.split("-")[0]))
        df["node2"] = df["fault_edge"].apply(lambda x: ord(x.split("-")[1]))

        df["path_label"] = df["path"].astype("category").cat.codes

        return df

    def train(self):
        df = pd.read_csv(self.data_path)

        # 🔥 CREATE PATH MAPPING
        categories = df["path"].astype("category").cat.categories
        path_mapping = dict(enumerate(categories))

        df = self.preprocess(df)

        X = df[["node1", "node2"]]
        y = df["path_label"]

        model = RandomForestClassifier()
        model.fit(X, y)

        # Save model
        with open(self.model_path, "wb") as f:
            pickle.dump(model, f)

        # Save mapping
        with open(self.mapping_path, "wb") as f:
            pickle.dump(path_mapping, f)

        print("✅ Model and mapping saved successfully!")


if __name__ == "__main__":
    trainer = ModelTrainer()
    trainer.train()