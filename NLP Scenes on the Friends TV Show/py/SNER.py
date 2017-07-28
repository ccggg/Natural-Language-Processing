# https://nlp.stanford.edu/software/CRF-NER.shtml

import nltk
import string
import re
from io import open
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn

# Stanford Named Entity Recognition Tagger.
st = StanfordNERTagger('G:/NER/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz',
					   'G:/NER/stanford-ner/stanford-ner.jar',
					   encoding='utf-8')

# Directory of the new keywords file without names included
f_new = "Z:/My Documents/Python/SciKit Learn/Test/keywords/Files/KeywordsNoNames.txt"
f = open(f_new, "w+")

# Directory of the old keywords file with names included
f_old = "Z:/My Documents/Python/SciKit Learn/Test/keywords/keywords.txt"

with open(f_old) as open_file:
    lines = open_file.readlines()
    for i in range(0, len(lines)):
        old_line = lines[i]

        old_line = old_line.replace("'s", "")
        #print old_line

        tokenized_text = word_tokenize(old_line)
        classified_text = st.tag(tokenized_text)

        final_line = ''
        for i in range(0, len(classified_text)):
            if classified_text[i][1] != 'PERSON':
                new_line = classified_text[i][0]
                new_line = re.sub(r'[^\w\s]','', new_line, re.UNICODE)
                new_line = new_line.lower()
                if new_line != '':
                    final_line = ' '.join([final_line, new_line]).strip()
                    #final_line = final_line + new_line
                    #print new_line,
            #print final_line
        print final_line
        f.write(unicode(final_line) + '\n')
