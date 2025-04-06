import nltk

nltk.download('wordnet')

from nltk.stem import  WordNetLemmatizer

wnl = WordNetLemmatizer()

list = ['kites', 'babies', 'apples', 'dogs', 'flying', 'died', 'tried', 'feet']

for words in list:
    print(words + "--->" + wnl.lemmatize(words))