'''Julia Marden and Jack Obrock'''

import functools
from functools import reduce

def mult(x, y):
    return x * y

def factorial(n):
    if n == 0:
        return 1
    else:
         return reduce(lambda x, y: x*y, range(1,n+1))

def dot_product(list1, list2):
  if len(list1) == len(list2):
      return reduce(lambda sum, p: sum + p[0] * p[1], zip(a, b), 0)

print(dot_product([1,2],[2,3]))

def count_vowels(string):
    string = input("Enter string:")
    vowels = 0
    for i in string:
        if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
            vowels = vowels + 1
    print("Number of vowels are:")
    print(vowels)

def check_ends(list):
    list = list(input('What is your list? '))
    return list[len(list)-1]


def starts_with_letter(letter, t) -> int:
    filter(lambda t: letter in t)
