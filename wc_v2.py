import sys

def main():
    try:
        file_name = sys.argv[1]
        f = open(file_name,'r')
        s = f.read()
        m = (map(lambda x: x if x.isalpha() else ' ', s))
        x = ''.join(m)
        lst = x.split()
        f.close()
        print("The file", file_name, "is", len(lst), "words long.")
        return(len(lst))
    except:
        print('I do not like what you got.')
        return None

if __name__ == '__main__':
    main()