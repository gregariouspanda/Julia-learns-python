import wc_unique

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

specific_word_count = wc_unique.main()
word_lengths = {}
for word in specific_word_count.keys():
    if len(word) not in word_lengths.keys():
        word_lengths[len(word)] = specific_word_count[word]
    else:
        word_lengths[len(word)] += specific_word_count[word]

objects = word_lengths.keys()
y_pos = np.arange(len(objects))
performance = word_lengths.values()

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.xlabel('Number of words')
plt.ylabel('Length of word')
plt.title('Number of words of a certain length')

# if __name__ == '__main__':
#     main()
plt.show()
