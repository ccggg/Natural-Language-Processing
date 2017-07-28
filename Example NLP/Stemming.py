from nltk.stem import PorterStemmer as ps
from nltk.tokenize import sent_tokenize, word_tokenize

ps = ps()

text = "It is important to by very pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once"
words = word_tokenize(text)

for w in words:
    print ps.stem(w)
