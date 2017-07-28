import os
import nltk
import linecache

from io import open
from nltk.tag import pos_tag
from nltk.corpus import wordnet as wn

file_dir = 'F:\Friends Natural Language Processing\scenes\scenes\KeywordsNoNames.txt'
new_file = open('F:\Friends Natural Language Processing\scenes\scenes\RawHypernyms.txt', "w")

with open(file_dir, 'r', encoding='utf-8-sig') as open_file:
        lines = open_file.readlines()

        line_num = 0
        with open(file_dir) as open_file:
            for line in open_file:
                line_num = line_num + 1
                print ''
                print line

                for i in range(0, len(line.split())):
                    word = line.split()[i]
                    word = word.replace(',', '')
                    word = word.replace('.', '')
                    word = word.replace("'", '')
                    word = word.replace("'s", '')

                    try:
                        syn = wn.synsets(word.split()[0])[0]
                        print syn
                        if syn.lexname() == 'noun.quantity':
                            syn = wn.synsets(word.split()[0])[1]
                    except IndexError:
                        print 'Nothing returned'
                        print ''

                    hyp_num = 4
                    while True:
                        try:
                            hyp = syn.hypernyms()[0]
                            for i in range(0, hyp_num):
                                hyp = hyp.hypernyms()[0]
                            print 'Hypernym: ' + str(hyp.name())
                            word = str(hyp.name()).split('.', 1)[0]
                            #word = word.replace('_', ' ')
                            new_file.write(unicode(word) + ' ')

                        except IndexError:
                            if hyp_num >= 0:
                                hyp_num = hyp_num - 1
                            else:
                                break
                            continue
                        break
                        hyp_num = 4
                new_file.write(unicode('{' + str(line_num) + '}'))
                new_file.write(unicode('\n'))
        new_file.close()

keywords_file = 'F:\Friends Natural Language Processing\scenes\scenes\KeywordsNoNames.txt'
hyp_file = 'F:\Friends Natural Language Processing\scenes\scenes\RawHypernyms.txt'
grouped_file = open('F:\Friends Natural Language Processing\scenes\scenes\GroupedScenes.txt', "w")

checked_groups = []

with open(hyp_file, "r+") as open_file:
    with open(keywords_file, "r") as key_file:
        lines = open_file.readlines()
        key_lines = key_file.readlines()
        for i in range(0, len(lines)):
            orig_word = unicode(lines[i].split('{', 1)[0])
            orig_num = unicode(lines[i].split('{', 1)[1])
            orig_num = orig_num.replace('}', '')
            if not any(orig_word in s for s in checked_groups):
                final_line = ''.join([key_lines[int(orig_num) - 1].strip('\n'), ' [' + lines[i].split(' {', 1)[0] + ']'])
                print(final_line)
                grouped_file.write(final_line)
                grouped_file.write(unicode('\n'))
                checked_groups.append(orig_word)
                for j in range(0, len(lines)):
                    other_word = unicode(lines[j].split('{', 1)[0])
                    other_num = unicode(lines[j].split('{', 1)[1])
                    other_num = other_num.replace('}', '')
                    if i != j and orig_word == other_word:
                        final_line = ''.join([key_lines[int(other_num) - 1].strip('\n'), ' [' + lines[j].split(' {', 1)[0] + ']'])
                        print(final_line)
                        grouped_file.write(final_line)
                        grouped_file.write(unicode('\n'))
