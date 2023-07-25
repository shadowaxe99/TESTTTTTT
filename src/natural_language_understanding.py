```python
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

class NaturalLanguageUnderstanding:
    def __init__(self):
        nltk.download('punkt')
        nltk.download('wordnet')
        nltk.download('stopwords')
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()

    def preprocess_text(self, text):
        word_tokens = word_tokenize(text)
        filtered_sentence = [w for w in word_tokens if not w in self.stop_words]
        lemmatized_sentence = [self.lemmatizer.lemmatize(w) for w in filtered_sentence]
        return lemmatized_sentence

    def understand(self, text):
        preprocessed_text = self.preprocess_text(text)
        # Here, you can add more complex NLU tasks such as Named Entity Recognition, Sentiment Analysis, etc.
        # For simplicity, we are just returning the preprocessed text
        return preprocessed_text
```