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

sorted_keys = list(sorted(word_lengths.keys()))
value = []
for key in sorted_keys:
	value.append(word_lengths[key])

y_pos = np.arange(len(value))

plt.bar(y_pos, value, align='center', alpha=0.5)
plt.xticks(y_pos, sorted_keys)plt.xlabel('Number of words')
plt.ylabel('Length of word')
plt.title('Number of words of a certain length')
plt.show()
