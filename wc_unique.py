import sys

def main():
    try:
        name = sys.argv[1]
        f = open(name,'r')
        s = f.read()
        m = (map(lambda x: x if x.isalpha() else ' ', s))
        x = ''.join(m)
        lst = x.split()
        words = {}
        for word in lst:
            if word not in words.keys():
                words[word] = 1
            else:
                words[word] += 1

        print(words)
        f.close()
        return(words)
    except:
        print('I do not like what you got.')
        return None

if __name__ == '__main__':
    main()