```python
import requests
from bs4 import BeautifulSoup

def scrape_product_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    product_data = {}
    product_data['name'] = soup.find('h1', {'class': 'product-name'}).text
    product_data['price'] = soup.find('span', {'class': 'product-price'}).text
    product_data['description'] = soup.find('div', {'class': 'product-description'}).text
    product_data['reviews'] = [review.text for review in soup.find_all('div', {'class': 'product-review'})]

    return product_data

def scrape_supplier_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    supplier_data = {}
    supplier_data['name'] = soup.find('h1', {'class': 'supplier-name'}).text
    supplier_data['rating'] = soup.find('span', {'class': 'supplier-rating'}).text
    supplier_data['location'] = soup.find('div', {'class': 'supplier-location'}).text
    supplier_data['products'] = [product.text for product in soup.find_all('div', {'class': 'supplier-product'})]

    return supplier_data

def scrape_market_trends(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    market_trends = {}
    market_trends['trending_products'] = [product.text for product in soup.find_all('div', {'class': 'trending-product'})]
    market_trends['popular_categories'] = [category.text for category in soup.find_all('div', {'class': 'popular-category'})]

    return market_trends
```