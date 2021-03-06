from bs4 import BeautifulSoup
import urllib2
import re

def extract_html():
    current_file = 101
    
    while current_file <= 124:
        print current_file
        print 'https://fangj.github.io/friends/season/0' + str(current_file) + '.html'
        #soup = BeautifulSoup(urllib2.urlopen('https://fangj.github.io/friends/season/0' + str(current_file) + '.html').read(), 'lxml')
        soup = BeautifulSoup(open('../../scenes/raw_html/0' + str(current_file) + '.html').read(), 'lxml')


        f = open("../../scenes/raw_txt/0" + str(current_file) + ".txt", "w+")
        [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
        f.write(re.sub(r'\n', r' ', soup.get_text().strip().encode('utf-8'), flags=re.M))

        in_scene = False
        with open("../../scenes/raw_txt/0" + str(current_file) + ".txt", 'r') as open_file:
            for line in open_file:
                for c in line:
                    if c == '[':
                        f.write('\n>' + c)
                        in_scene = True
                    elif c == ')' and in_scene:
                        f.write(']')
                        in_scene = False
                    elif c == ']':
                        f.write(c)
                        in_scene = False
                    elif in_scene:
                        f.write(c + '')

        f.close()
        current_file += 1
