import fileinput
import re

f = open('strongs.txt', 'r')

for line in f:
    if line[0] == '-':
        domain = line
    else:
        line = line[:-1]
        g = open('wiki/'+line+'.txt', 'r', newline="\n")
        h = open('clean/'+line+'_clean.txt', 'w')

        text = g.read()
        text = re.sub(r'(?s)<mediawiki(.*?){{Infobox', '', text)
        text = re.sub(r'&lt;.*?&gt;', '', text)
        text = re.sub(r"\[\[([^\|]*?)\]\]", r"\1", text)
        text = re.sub(r"\[\[(.*?)\|(.*?)\]\]", r"\2", text)
        text = re.sub(r'\{\{[cC]ite.*?\}\}', '', text)
        text = re.sub(r'&amp;nbsp;', '', text)
        text = re.sub(r'&amp;', '&', text)
        text = re.sub(r'(?s)==References==.*', '', text)
        text = re.sub('\n\|', '. '+'\n', text)

        h.write(text)

g.close()
h.close()

'''

import re

g = open('strongs.txt', 'r')
text = g.read()
g.close()

g = open('strongs.txt', 'w')
text = re.sub('\n', '\n', text)
g.write(text)
g.close()

'''
