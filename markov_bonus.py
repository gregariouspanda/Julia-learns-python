import random
import sys
import string

def create_dictionary(file_name, context_length):
    f = open(file_name,'r')
    s = f.read()
    rlst=s.split()
    lst = list(map(lambda word: word.replace('"',''), rlst))
    words = {'$':[lst[0]]}
    for index, word in enumerate(lst[:-context_length]):
        key = tuple(lst[index:(index+context_length)])
        if key[-1][-1] in '.!?':
            key = '$'
        if key not in words.keys():
            words[key] = []
        words[key].append(lst[index + context_length])
    #print(words)
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
            choices = word_dict[tuple()]
        except:
            pass
        last_word_added = random.choice(choices)
        story += ' ' + last_word_added
        if last_word_added[-1] in '.!?':
           last_word_added = '$'
        words += 1
    return story

def main():
    context_length = int(sys.argv[2])
    #num_words = sys.argv[3]
    word_dict = create_dictionary(sys.argv[1], context_length)
    #f = open(sys.argv[2],'w')
    #f.write(generate_story(word_dict, int(num_words)))
    #f.close()

if __name__ == '__main__':
    main()