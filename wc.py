def main():
    f = open('spam.txt','r')
    s = f.read()
    m = (map(lambda x: x if x.isalpha() else ' ', s))
    x = ''.join(m)
    lst = x.split()
    f.close()
    print(len(lst))
    return(len(lst))

if __name__ == '__main__':
    main()