```python
import json
import pandas as pd

def load_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file)

def load_csv(file_path):
    return pd.read_csv(file_path)

def save_csv(data, file_path):
    data.to_csv(file_path, index=False)

def validate_product_schema(data, product_schema):
    for key in product_schema.keys():
        if key not in data:
            return False
    return True

def validate_user_schema(data, user_schema):
    for key in user_schema.keys():
        if key not in data:
            return False
    return True
```