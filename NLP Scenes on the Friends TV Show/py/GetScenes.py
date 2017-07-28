import os
import time
import HTML
#import ExtractKeywords
from msvcrt import getch

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    print 'Press the corresponding key for the action'
    print 'Result is output into text files'
    print ''
    print '1. Run scene extraction code to get scenes in text format from HTML files'
    print '2. Run RAKE algorithm on scenes to remove unnecessary words'
    print '3. Run Stanford Named Entity Recognition on scenes to remove peoples names'
    print '4. Run WordNet code to get Hypernyms of each word in scenes'

if __name__ == "__main__": main()

while True:
    key = ord(getch())
    if key == 49: # 1
        print 'Pressed 1'
        clear_screen()
        HTML.extract_html()
        time.sleep(2)
        main()
    elif key == 50: # 2
        print 'Pressed 2'
        clear_screen()
        print 'EXECUTE CODE'
        time.sleep(2)
        main()
    elif key == 51: # 3
        print 'Pressed 3'
        clear_screen()
        print 'EXECUTE CODE'
        time.sleep(2)
        main()
    elif key == 52: # 3
        print 'Pressed 4'
        clear_screen()
        print 'EXECUTE CODE'
        time.sleep(2)
        main()
