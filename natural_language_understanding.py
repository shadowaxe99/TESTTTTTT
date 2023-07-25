```python
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

class NaturalLanguageUnderstanding:
    def __init__(self):
        nltk.download('punkt')
        nltk.download('stopwords')
        self.stop_words = set(stopwords.words('english'))

    def understand_language(self, text):
        tokenized = sent_tokenize(text)
        for i in tokenized:
            words = nltk.word_tokenize(i)
            words = [word for word in words if word.isalnum()]
            words = [word for word in words if not word in self.stop_words]
            tagged = nltk.pos_tag(words)
            return tagged

if __name__ == "__main__":
    nlu = NaturalLanguageUnderstanding()
    text = "The market trend for this month shows an increase in demand for electronic gadgets."
    print(nlu.understand_language(text))
```