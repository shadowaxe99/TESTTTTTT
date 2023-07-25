```python
import requests
from bs4 import BeautifulSoup

# Define the APIs
product_listing_API = "http://example.com/api/product_listings"
customer_order_API = "http://example.com/api/customer_orders"
supplier_info_API = "http://example.com/api/supplier_info"

# Define the web scraping functions
def scrape_product_listings():
    response = requests.get(product_listing_API)
    soup = BeautifulSoup(response.text, 'html.parser')
    product_listings = soup.find_all('div', class_='product-listing')
    return product_listings

def scrape_customer_orders():
    response = requests.get(customer_order_API)
    soup = BeautifulSoup(response.text, 'html.parser')
    customer_orders = soup.find_all('div', class_='customer-order')
    return customer_orders

def scrape_supplier_info():
    response = requests.get(supplier_info_API)
    soup = BeautifulSoup(response.text, 'html.parser')
    supplier_info = soup.find_all('div', class_='supplier-info')
    return supplier_info

# Define the real-time data integration function
def integrate_data():
    product_listings = scrape_product_listings()
    customer_orders = scrape_customer_orders()
    supplier_info = scrape_supplier_info()

    # Combine the data into a single data structure for further processing
    data = {
        'product_listings': product_listings,
        'customer_orders': customer_orders,
        'supplier_info': supplier_info
    }

    return data
```