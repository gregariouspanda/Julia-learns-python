import sys
import re

# Returns a list of words from a file, with all of the newlines stripped out
def read_file(file_name):
    #f(x) = read in the characters from file x
    #g(x) = substitute the non-letter characters with spaces in a list of characters x
    #h(x) = join a list x of characters into a single string with '' between character
    #i(x) = split a string at space boundaries
    #i(h(g(f(x))))

    return ''.join(
                re.sub(
                  re.compile('[^a-z]', re.IGNORECASE),
                  ' ',
                  open(file_name, 'r').read()
                )
              ).split()

def main():
    lst = read_file(sys.argv[1])
    words = {}
    for word in lst:
        if word not in words.keys():
            words[word] = 1
        else:
            words[word] += 1

    print(words)
    return(words)

if __name__ == '__main__':
    main()
