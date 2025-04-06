import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')
sentence = "Today is a snowy day in Baku."
tokens = word_tokenize(sentence)

stopwords = set(stopwords.words("english"))

filtered_tokens = [word for word in tokens if word.lower() not in stopwords]

print(filtered_tokens)
