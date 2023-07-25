```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from src.config import product_schema

class MachineLearningModels:
    def __init__(self, data):
        self.data = data
        self.model = None

    def preprocess_data(self):
        self.data = pd.DataFrame(self.data, columns=product_schema)
        self.data.dropna(inplace=True)

    def split_data(self):
        X = self.data.drop('profit_margin', axis=1)
        y = self.data['profit_margin']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
        return X_train, X_test, y_train, y_test

    def train_model(self):
        X_train, X_test, y_train, y_test = self.split_data()
        self.model = RandomForestRegressor(n_estimators=100, random_state=0)
        self.model.fit(X_train, y_train)
        predictions = self.model.predict(X_test)
        print("Model Trained. MAE: ", mean_absolute_error(y_test, predictions))

    def get_model(self):
        return self.model

if __name__ == "__main__":
    from src.data_collection_preprocessing import DataCollectionPreprocessing
    data_collector = DataCollectionPreprocessing()
    data = data_collector.collect_data()
    data_collector.preprocess_data()
    ml_models = MachineLearningModels(data)
    ml_models.preprocess_data()
    ml_models.train_model()
```