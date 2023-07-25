```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load preprocessed data
data = pd.read_csv('preprocessed_data.csv')

# Define features and target
features = data.drop('is_promising', axis=1)
target = data['is_promising']

# Split data into training and testing sets
features_train, features_test, target_train, target_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Initialize the model
model = RandomForestClassifier(n_estimators=100, random_state=42)

def train_model(features_train, target_train):
    # Train the model
    model.fit(features_train, target_train)

def predict_item(features_test):
    # Make predictions
    predictions = model.predict(features_test)
    return predictions

def evaluate_model(target_test, predictions):
    # Evaluate the model
    accuracy = accuracy_score(target_test, predictions)
    return accuracy

# Train the model
train_model(features_train, target_train)

# Make predictions
predictions = predict_item(features_test)

# Evaluate the model
accuracy = evaluate_model(target_test, predictions)
print(f'Model Accuracy: {accuracy}')

# Save the trained model for future use
import joblib
joblib.dump(model, 'drop_shipping_model.pkl')
```