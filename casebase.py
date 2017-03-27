from itertools import product

passbase = raw_input("Please enter the base password: ")

keywords = [''.join(i) for i in product(passbase, repeat = len(passbase))]

for passwd in keywords:
    print passwd
