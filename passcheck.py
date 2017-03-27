from itertools import product
from string import ascii_lowercase
from string import ascii_letters

keywords = [''.join(i) for i in product(ascii_letters, repeat = 3)]

print len(keywords)

# passbase = raw_input("Please enter the base password: ")
#
# for prefix in keywords:
#     print prefix + passbase
