def stemming_AZE(word):
    if "lar" in word or "lər" in word:
        word = word.replace("lar", "").replace("lər", "")
    return word

text = "Sona bülbüllər bulaq üstündə uçurdular"

stemmed_words = [stemming_AZE(word) for word in text.split()]

print(text)

print(stemmed_words)