'''Julia Marden and Giulia De Gennaro'''
mode = input('Do you want to encrypt, fox encrypt, decrypt, or fox decrypt your message? (e, f, d, x) ')
import random


upperfoxlist = ['T','H','E','Q','U','I','C','K','B','R','O','W','N','F','X','J','M','P','S','V','L','A','Z','Y','D','G']
lowerfoxlist = ['t','h','e','q','u','i','c','k','b','r','o','w','n','f','x','j','m','p','s','v','l','a','z','y','d','g']

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


def upper_fox_encryption(letter, shift):
    try:
        letter_index = upperfoxlist.index(letter)
        if (letter_index + shift) < 26:
            return upperfoxlist[letter_index + shift]
        elif (letter_index + shift) >= 26:
            return upperfoxlist[-(26- (letter_index+shift))]
    except ValueError:
        return None


def lower_fox_encryption(letter,shift):
    try:
        letter_index = lowerfoxlist.index(letter)
        if (letter_index + shift) < 26:
            return lowerfoxlist[letter_index + shift]
        elif (letter_index + shift) >= 26:
            return lowerfoxlist[-(26-(letter_index+shift))]
    except ValueError:
        return None


def fox_encryption(letter, shift):
    if ord(letter) <= 64 or 91 <= ord(letter) <= 96 or ord(letter) >= 123:
        return letter
    elif 65 <= ord(letter) <= 90:
        return upper_fox_encryption(letter, shift)
    elif 97 <= ord(letter) <= 122:
        return lower_fox_encryption(letter, shift)


def new_message(listmessage, encription_func, shift):
    newlist = [encription(listmessage[i], shift) for i in range(len(listmessage))]
    return newlist

def new_fox_message(listmessage, encription_func, shift):
    #newlist = [encription(listmessage[i], shift) for i in range(len(listmessage))]
    newlistfox = [fox_encryption(listmessage[i], shift) for i in range(len(listmessage))]
    return newlistfox

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

def fox_frequency(letter):
    for letter in upperfoxlist:
        if 0 <= letter.index(upperfoxlist) <= 25:
            letter = lowerfoxlist[letter.index(upperfoxlist)]
        elif letter < 0 or letter > 25:
            return 0
        foxfrequencies = [9.056, 6.094, 12.702, 0.095,
                          2.758, 6.966, 2.782, 0.772, 1.492,
                          5.987, 7.507, 2.36, 6.74, 2.228,
                          0.15, 0.153, 2.406, 1.929, 6.327,
                          0.978, 4.025, 8.167, 0.074, 1.974, 4.253, 2.015]
        return foxfrequencies[letter.index(lowerfoxlist)]


def frequency_score(words):
    return sum(map(letter_frequency, words))
def fox_frequency_score(words):
    return sum(map(fox_frequency, words))

if mode == 'e':
    message = input('What message do you want to send? ')
    shiftchoice = input("How much do you want to shift the letters? (If you're indecisive, write 'surprise me!') ")
    if shiftchoice == 'surprise me!':
        shift = random.randint(1,26)
    else:
        shift = int(shiftchoice)
    listmessage = list(message)
    print(''.join(new_message(listmessage, encription, shift)))

elif mode == 'f':
    message = input('What message do you want to send? ')
    shiftchoice = input("How much do you want to shift the letters? (If you're indecisive, write 'surprise me!') ")
    if shiftchoice == 'surprise me!':
        shift = random.randint(1, 26)
    else:
        shift = int(shiftchoice)
    listmessage = list(message)
    print(''.join(new_fox_message(listmessage, encription, shift)))


elif mode == 'd':
    message1 = input('What is the message you want to decrypt? ')
    listmessage1 = list(message1)
    decrypted_strings = []
    for shift in range(26):
        decrypted_strings.append(new_message(listmessage1, encription, shift))
    bestscore = 0
    best_score_shift = 0
    for shift in range(26):
        this_score = frequency_score(decrypted_strings[shift])
        if this_score > bestscore:
            bestscore = this_score
            best_score_shift = shift
    print(''.join(decrypted_strings[best_score_shift]))

elif mode == 'x':
    message1 = input('What is the message you want to decrypt? ')
    listmessage1 = list(message1)
    decrypted_fox = []
    decrypted_strings = []
    for shift in range(26):
        decrypted_fox.append(new_fox_message(listmessage1, fox_encryption, shift))
        print(''.join(decrypted_fox[shift]))
    bestscore = 0
    #best_score_shift = 0
    #for shift in range(26):
       # this_score = fox_frequency(decrypted_fox[shift])
       # if this_score > bestscore:
            #bestscore = this_score
           # best_score_shift = shift
    #print(''.join(decrypted_fox[best_score_shift]))




    brutethisbish = input('This decryption may not be correct, would you like to see the list of all possible decryptions?(y/n) ')
    if brutethisbish == 'y':
        for shift in range(26):
            print(''.join(new_message(listmessage1,encription,shift)))
else:
    print('I do not like what you got.')


