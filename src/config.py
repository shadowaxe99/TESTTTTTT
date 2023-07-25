```python
# src/config.py

# Database configuration
DATABASE_CONFIG = {
    'host': 'localhost',
    'database': 'dropship_db',
    'user': 'root',
    'password': 'password'
}

# API configuration
API_CONFIG = {
    'api_key': 'your_api_key',
    'api_secret': 'your_api_secret'
}

# Web scraping configuration
WEB_SCRAPING_CONFIG = {
    'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Machine learning model configuration
MODEL_CONFIG = {
    'model_path': 'models/dropship_model.pkl'
}

# Natural language understanding configuration
NLU_CONFIG = {
    'nlu_model_path': 'models/nlu_model.pkl'
}

# Flask/Django app configuration
APP_CONFIG = {
    'secret_key': 'your_secret_key',
    'debug': True
}
```