import sys
import string

def create_dictionary(file_name):
    f = open(file_name,'r')
    s = f.read()
    rlst=s.split()
    lst = ['$']
    for word in rlst:
        if word[-1] in string.punctuation:
            lst.append(word[:-1])
            if word[-1] == ',':
                lst.append(word[-1])
            else:
                lst.append('$')
        else:
            lst.append(word)

    words = {}
    for index, word in enumerate(lst[:-1]):
        if word not in words.keys():
            words[word] = []

        words[word].append(lst[index + 1])
    return (words)
