import random
import sys
import string

def create_dictionary(file_name):
    f = open(file_name,'r')
    s = f.read()
    rlst=s.split()
    lst = ['$']+ list(map(lambda word: word.replace('"',''), rlst))
    words = {}
    for index, word in enumerate(lst[:-1]):
        key = word
        if word[-1] in '.!?':
            key = '$'
        if key not in words.keys():
            words[key] = []
        words[key].append(lst[index + 1])
    return (words)


def generate_story(word_dict, num_words):
    story = ''
    words = 0
    last_word_added = random.choice(word_dict['$'])
    story += last_word_added
    words += 1

    while words < num_words:
        choices = word_dict['$']
        try:
            choices = word_dict[last_word_added]
        except:
            pass
        last_word_added = random.choice(choices)
        story += ' ' + last_word_added
        if last_word_added[-1] in '.!?':
           last_word_added = '$'
        words += 1
    return story

def main():
    num_words = sys.argv[3]
    word_dict = create_dictionary(sys.argv[1])
    f = open(sys.argv[2],'w')
    f.write(generate_story(word_dict, int(num_words)))
    f.close()

if __name__ == '__main__':
    main()
