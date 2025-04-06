import nltk
from nltk.tokenize import word_tokenize

"Tokenization by using library"
nltk.download('punkt')
sentence = "Today is a snowy day in Baku."
tokens = word_tokenize(sentence)
print(tokens)


# Simple tokenizatioon example
"""
sentence = "Today is a snowy day in Baku."
tokens = sentence.split()

print(tokens)
"""


