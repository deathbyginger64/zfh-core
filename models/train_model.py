import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
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

        print("\n📊 Dataset Preview:")
        print(df.head())

        # Mapping
        categories = df["path"].astype("category").cat.categories
        path_mapping = dict(enumerate(categories))

        df = self.preprocess(df)

        # 🔥 ALL FEATURES
        feature_cols = ["node1", "node2", "num_active_links"]
        weight_cols = [col for col in df.columns if "_weight" in col]
        feature_cols += weight_cols

        X = df[feature_cols]
        y = df["path_label"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        print(f"\n📊 Training samples: {len(X_train)}")
        print(f"📊 Testing samples: {len(X_test)}")

        model = RandomForestClassifier()
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)

        print(f"\n🎯 Model Accuracy: {accuracy:.2f}")

        with open(self.model_path, "wb") as f:
            pickle.dump(model, f)

        with open(self.mapping_path, "wb") as f:
            pickle.dump(path_mapping, f)

        print("\n✅ Model and mapping saved successfully!")


if __name__ == "__main__":
    trainer = ModelTrainer()
    trainer.train()