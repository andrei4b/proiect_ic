import urllib.request
import re

f = open('strongs.txt', 'r')

for line in f:
    if line[0] == '-':
        domain = line
    else:
        response = urllib.request.urlopen('https://en.wikipedia.org/wiki/Special:Export/' + line)
        html = response.read()#.decode('utf-8').encode()
        line = line[:-1]
        g = open('wiki/' + line + '.txt', 'w', newline='\r\n')
        g.write(domain)
        #html = re.sub('\n', '\n', html.decode('ascii', 'ignore'))
        g.write(html.decode('ascii', 'ignore'))
        g.close()

f.close()





