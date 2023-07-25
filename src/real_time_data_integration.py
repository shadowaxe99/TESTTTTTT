```python
import requests
from bs4 import BeautifulSoup
from src.config import API_URL, WEB_SCRAPING_URL
from src.utils import update_product_schema

def update_data():
    # Update data using APIs
    response = requests.get(API_URL)
    data = response.json()
    update_product_schema(data)

    # Update data using web scraping
    response = requests.get(WEB_SCRAPING_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    product_listings = soup.find_all('div', class_='product-listing')
    for product in product_listings:
        data = {
            'name': product.find('h2').text,
            'price': product.find('span', class_='price').text,
            'supplier': product.find('span', class_='supplier').text,
            'availability': product.find('span', class_='availability').text
        }
        update_product_schema(data)
```