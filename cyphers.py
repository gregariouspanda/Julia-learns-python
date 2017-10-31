'''Julia Marden and Giulia De Gennaro'''
mode = input('Do you want to encrypt or decrypt your message?(e/d) ')

def encription(letter, shift):
    if ord(letter) <= 64 or 91 <= ord(letter) <= 96 or ord(letter) >= 123:
        return letter
    elif ord(letter) <= 90:
        if ord(letter) + shift <= 90:
            return chr(ord(letter) + shift)
        else:
            return chr(65 + shift - (90 - ord(letter)) - 1)
    else:
        if ord(letter) + shift <= 122:
            return chr(ord(letter) + shift)
        else:
            return chr(97 + shift - (122 - ord(letter)) - 1)

def new_message(listmessage, encription_func, shift):
    newlist = [encription(listmessage[i], shift) for i in range(len(listmessage))]
    return (newlist)

def letter_frequency(c):
    if 'A' <= c <= 'Z':
        c = c.lower()
    if c < 'a' or c > 'z':
        return 0
    frequencies = [8.167, 1.492, 2.782, 4.253, 12.702,
                    2.228, 2.015, 6.094,
                    6.966, 0.153, 0.772, 4.025, 2.406, 6.749, 7.507,
                    1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.36,
                    0.15, 1.974, 0.074]
    return frequencies[ord(c) - ord('a')]

# This is what map() is all about.
# 1. Take a list of letters, aka list(some_string)
# 2. For each letter, compute the letter_frequency for that letter
#    In other words, "map" the letter to its letter frequency score
# 3. The result of the mapping is a list of floats. Specifically, it
#    is a list of the letter frequency scores that correspond to the
#    characters in the original string. Sum up those floats to get
#    the frequency score for the entire string.
#
#    sum of,
#      the mapping to scores of,
#        the list of letters
#
#    It's just composite functions in algebra/calculus all over again :-)
def frequency_score(some_list_of_characters):
  return sum(map(letter_frequency, some_list_of_characters))

if mode == 'e':
    message = input('What message do you want to send? ')
    shift = int(input('How much do you want to shift the letters? '))
    listmessage = list(message)

    print(''.join(new_message(listmessage, encription, shift)))

elif mode == 'd':
    message1 = input('What is the message you want to decrypt? ')
    listmessage1 = list(message1)

    decrypted_strings = []
    for shift in range(26):
        # Each entry in the decrypted_strings list is itself a list
        # of (decrypted) characters.
        decrypted_strings.append(new_message(listmessage1, encription, shift))

    best_score = 0
    best_score_shift = 0

    for shift in range(26):
        this_score = frequency_score(decrypted_strings[shift])
        if this_score > best_score:
            best_score = this_score
            best_score_shift = shift

    print(''.join(decrypted_strings[best_score_shift]))

    brutethisbish = input('This decryption may not be correct, would you like to see the list of all possible decryptions?(y/n) ')
    for shift in range(26):
        if brutethisbish == 'y':
            print(''.join(new_message(listmessage1,encription,shift)))
        elif brutethisbish == 'n':
            print('Alright, peace out!')
else:
    print('I do not like what you got.')


