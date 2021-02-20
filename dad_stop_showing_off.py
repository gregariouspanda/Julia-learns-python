'''Flamingo, by the immortal Herb Jeffries'''

year = int(raw_input("What year were you born? "))

if year == 1971:
  print "You must be pretty cool to have been born in " + str(year) + "."
else:
  print "Well we can't all be cool I suppose."

print "You are about " + str(2017 - year) + " years old."

# Here are four random animals
oreilly_cover_animals = ["aardvark", "bonobo", "camel", "dik-dik"]

'''random.randint(0,3) will always be 0, 1, 2, or 3

As a result, the index value used in oreilly_cover_animals
will never be "out of bounds" (less than 0 or greater than 3)'''
import random
print "Your spirit animal is a " + oreilly_cover_animals[random.randint(0,3)]

""" Same trick for any cyclical data structure

By taking % N you always guarantee a number between 0 and N"""
chinese_year_animals = [
  "rat", "ox", "tiger", "rabbit", "dragon", "snake",
  "horse", "goat", "monkey", "rooster", "dog", "pig"
]

'''
Note that 1912 is an arbitary choice for zodiac_start_year. I could have
chosen any Year of the Rat.  Why? Because all I want is a year such
that year - zodiac_start_year is:

(N*12 + 0) for anyone born in the Year of the Rat
(N*12 + 1) for anyone born in the Year of the Ox
(N*12 + 2) for anyone born in the Year of the Tiger
...
etc.

So imagine your birth year is 1948. By the math I'm using then

1948 - zodiac_start_year = 1948 - 1912 = 36
but 36 = 3*12 + 0, and (3*12 + 0) % 0 = 0 ==> chinese_year_animals[0] => 'rat'

But I also could have chosen my zodiac_start_year to be 1900. Then

1948 - zodiac_start_year = 1948 - 1900 = 48
but 48 = 4*12 + 0, and (4*12 + 0) % 0 = 0 ==> chinese_year_animals[0] => 'rat'

I even could have chosen my zodiac_start_year to be 1960!

1960 - zodiac_start_year = 1948 - 1960 = -12
but -12 = -1*12 + 0, and (-1*12 + 0) % 0 = 0 ==> chinese_year_animals[0] => 'rat'

So the choice of zodiac_start_year doesn't matter as long as it's a year that
corresponds with the zeroth element in the chinese_year_animals array. It even
works when the zodiac_start_year is later than the input year, because we're
just going around in circles of length 12 years, backwards or forwards, it
doesn't matter.

Extra credit for smarty-pants: I could also put "ox" as the zeroth element
in the chinese_year_animals array and use 1913 or 1925 or 1937 as my "year 0".

If I did that, where would "rat" go in the chinese_year_animals array?
Think about it!
'''
zodiac_start_year = 1912
your_animal = chinese_year_animals[(year - zodiac_start_year) % 12]
print "But unfortunately your Chinese zodiac animal is just a lame old " + your_animal + "."
