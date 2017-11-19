import random
import sys
import string

# Returns a list containing all of the words in a file
# (in order), with double-quotes stripped out.

def words_from_file(file_name):
    f = open(file_name,'r')
    contents = f.read()
    contents_without_quotes = contents.replace('"', '')
    return contents_without_quotes.split()

# Returns the longest possible (backwards-looking)
# context tuple beginning at the start of the provided
# "context" list and going until (but not including)
# an end-of-sentence word, or until context_length
# words are reached, whichever comes first.
#
# Examples:
#
# context_tuple(['donuts', 'like', 'I'], 2) returns ('donuts', 'like')
# context_tuple(['spam', 'is', 'It', 'bacon.', 'not'], 5) returns ('spam', 'is', 'It')
# context_tuple(['Now!', 'it!', 'Do'], 3) returns ()

def context_tuple(context, context_length):
    result = []
    for word in context:
        if word[-1] in '.!?':
            break
        else:
            result.append(word)
            if len(result) == context_length:
                break

    return tuple(result)

def create_dictionary(file_name, context_length):
    rlst = list(reversed(words_from_file(file_name)))

    words = {}

    for index, word in enumerate(rlst):
        context = context_tuple(rlst[index+1:], context_length)
        if context not in words.keys():
            words[context] = []
        words[context].append(word)

    return (words)

def generate_story(word_dict, num_words, context_length):
    long_story = [random.choice(word_dict[()])]

    while (len(long_story) < num_words) or (long_story[0][-1] not in '.?!'):
        context = context_tuple(long_story, context_length)
        long_story.insert(0, random.choice(word_dict[context]))

        # If we generate a context that does not occur
        # in the training text with following text, it's
        # probably the context of length context_length
        # that occurs exactly at the end of the training
        # file without punctuation.
        #
        # In that case, act as if the prior word had a
        # punctuation mark and start a new sentence.

        if context_tuple(long_story, context_length) not in word_dict.keys():
            long_story[0] = long_story[0] + random.choice(['.', '!', '?'])

    # Determine the longest story less than
    # num_words which ends in a full sentence.

    short_story = list(long_story)
    short_story = short_story[-num_words:]
    while short_story[0][-1] not in '.!?':
        short_story.pop(0)

    # In order to make the new story end
    # with proper punctuation, the program finds the
    # closest sentence end to the requested length.

    diff_long_story = len(long_story) - num_words
    diff_short_story = num_words - len(short_story)
    story = short_story
    if diff_long_story < diff_short_story:
        story = long_story

    return ' '.join(reversed(story))

def main():
    context_length = int(sys.argv[4])
    num_words = int(sys.argv[3])
    word_dict = create_dictionary(sys.argv[1], context_length)
    f = open(sys.argv[2], 'w')
    f.write(generate_story(word_dict, num_words, context_length))
    f.close()

if __name__ == '__main__':
    main()
