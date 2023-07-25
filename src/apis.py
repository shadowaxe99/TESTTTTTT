```python
import requests
import json

class APIManager:
    def __init__(self):
        self.headers = {'Content-Type': 'application/json'}

    def get_product_data(self, url):
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            return None

    def get_customer_orders(self, url):
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            return None

    def get_supplier_info(self, url):
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            return None

    def get_market_trends(self, url):
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            return None

    def get_customer_preferences(self, url):
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            return None
```