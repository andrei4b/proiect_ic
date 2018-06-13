import nltk
import re
nltk.download('punkt')

from nltk.tokenize import sent_tokenize


x = open('strongs.txt', 'r')

for line in x:
    if line[0] == '-':
        domain = line
    else:
        line = line[:-1]

        f = open('clean/'+line+'_clean.txt', 'r', newline='\r\n')
        g = open('split/'+line+'_split.txt', 'w')

        class Info:
                title = ""
                keywords = []
                sentences = []

                def __init__(self, title, keywords, sentences=None):
                        self.title = title
                        self.keywords = keywords
                        if sentences is None:
                                self.sentences = []
                        else:
                                self.sentences = sentences
                def __str__(self):
                        if not self.sentences:
                                return ''
                        else:
                                s = ''
                                for str in self.keywords:
                                        s+="'"+str+"'"+' '
                                s+='\n'
                                for sentence in self.sentences:
                                        s+=sentence + '\n______________________________\n'
                                return '\n' + "______"+self.title.upper()+"______" + '\n' + s

        h = open('info.txt', 'r', newline='\r\n')
        infos = []
        for sentence in h:
                sentence = sentence[:-3]
                words = sentence.split(',')
                '''for word in words:
                        if ' ' in word:
                                print("'" + word + "'")'''
                value = Info(words[0], words[1:])
                infos.append(value)

        for info in infos:
                print(info)

        sent_list = sent_tokenize(f.read())
        i=0

        for sentence in sent_list:
                i+=1
                #sentence = re.sub('\r\n', '', sentence)
                #g.write(sentence)
                #g.write('***********************************\n')
                for info in infos:
                        #ok = 0
                        for kw in info.keywords:
                                if (sentence not in info.sentences) and (kw in sentence) :
                                        info.sentences.append(sentence)
                                        print(info.title," ",i)
                                        #ok = 1

        for info in infos:
                g.write(str(info))

        f.close()
        g.close()
        h.close()

x.close()
