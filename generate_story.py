import sys
import create_dictionary
import random

def main():
    num_words = sys.argv[2]
    word_dict = create_dictionary.create_dictionary(sys.argv[1])
    print(generate_story(word_dict, int(num_words)))

def generate_story(word_dict, num_words):

    story = ''
    words = 0

    last_word_added = word_dict['$'][random.randint(0, len(word_dict['$'])-1)]
    story += last_word_added
    words += 1

    while words < num_words:
         last_word_added = word_dict[last_word_added][random.randint(0, len(word_dict[last_word_added])-1)]
         if last_word_added == '$':
             story += ". "
         else:
            story += ' ' + last_word_added
         words += 1

    return story

if __name__ == '__main__':
    main()



