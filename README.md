# Natural-Language-Processing

# Description
This program extracts the contents of the HTML transcripts, another script then extracts the scenes alone. The keywords can then be extracted from the scenes using the Rake algorithm scripts. The human names are then removed from the scenes using the Stanford Named Entity Recognition (SNER) script. The WordNet script then takes the scenes and converts all of the words into hypernyms, sentences with the same hypernyms are then grouped together and output into the text file in 'txt > scenes > GroupedScenes.txt'. 

# Software Requirements
* Anaconda 2 32-Bit https://repo.continuum.io/archive/Anaconda2-4.4.0-Windows-x86.exe
* Atom Text Editor (recommeneded) https://atom.io/

# Atom Setup Guide
* Install packages: **atom-pyton-run**, **autocomplete-python**, **python-indent**, **python-tools**
* Open settings for **atom-python-run**, for 'Command of F5' enter the directory for python.exe in Anaconda to e.g **D:\Anaconda2x86\python.exe "{file}"**

# Contents
* Example NLP - Scripts used for practise work which, some of which are included in the main program.
* NLP Scenes on the Friends TV Show - Takes the scene descriptions from the Friends TV show and groups them together based on hypernyms.

# What Needs Doing
* Extracting more words from each of the scene descriptions, they are still too broad to be able to get a general description.
