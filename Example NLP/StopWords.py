from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text = 'This is some example text, demonstrating the removal of stop words in NLTK.'
stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(text)

filtered_sentence = [w for w in word_tokens if not w in stop_words]

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

print word_tokens
print filtered_sentence
