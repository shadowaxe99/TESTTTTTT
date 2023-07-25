```python
import pandas as pd
from src.apis import get_product_data, get_order_data, get_supplier_data
from src.utils import clean_data

def collect_data():
    product_data = get_product_data()
    order_data = get_order_data()
    supplier_data = get_supplier_data()

    return product_data, order_data, supplier_data

def preprocess_data(product_data, order_data, supplier_data):
    product_df = pd.DataFrame(product_data)
    order_df = pd.DataFrame(order_data)
    supplier_df = pd.DataFrame(supplier_data)

    product_df = clean_data(product_df)
    order_df = clean_data(order_df)
    supplier_df = clean_data(supplier_df)

    return product_df, order_df, supplier_df

if __name__ == "__main__":
    product_data, order_data, supplier_data = collect_data()
    product_df, order_df, supplier_df = preprocess_data(product_data, order_data, supplier_data)

    data = {
        'product_data': product_df,
        'order_data': order_df,
        'supplier_data': supplier_df
    }
```
