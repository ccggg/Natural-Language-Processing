import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

# Some example text
text = "This is some example text. This example text is going to demonstrate NLTK tokenization. Does it work? Names like Mr. Smith and Mrs. Smith shouldn't separate, even though Mr. contains a period."

# Tokenize by sentence
print sent_tokenize(text)

print ''

# Tokenize by word
print word_tokenize(text)
