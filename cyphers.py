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

if mode == 'e':
    message = input('What message do you want to send? ')
    shift = int(input('How much do you want to shift the letters? '))
    listmessage = list(message)

    print(''.join(new_message(listmessage, encription, shift)))

elif mode == 'd':
    message1 = input('What is the message you want to decrypt? ')
    listmessage1 = list(message1)
    freqall = []
    for i in range(26):
        shift = i
        decrypt = new_message(listmessage1, encription, shift)
        frequency = []
        (map(letter_frequency, decrypt))
        for i in range(len(decrypt)):
            frequency.append(letter_frequency(decrypt[i]))
        freqall.append(sum(frequency))
    for x in freqall:
        if x == max(freqall):
            print(''.join(decrypt))

    brutethisbish = input('This decryption may not be correct, would you like to see the list of all possible decryptions?(y/n) ')
    if brutethisbish == 'y':
        print(''.join(new_message(listmessage1,encription,shift)))
    elif brutethisbish == 'n':
       print('Alright, peace out!')





else:
    print('I do not like what you got.')


