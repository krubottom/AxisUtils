from itertools import product
from string import ascii_lowercase
from string import ascii_letters
from string import ascii_uppercase

passbase = raw_input("Please enter the base password: ")
camaddr = raw_input("Please enter the camera IP address: ")

keywords = [''.join(i) for i in product(ascii_uppercase, repeat = 3)]

for prefix in keywords:
    print prefix + passbase

print "Generated " + str(len(keywords)) + " passwords"
