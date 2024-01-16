#!/usr/bin/python3

import string
alp = string.ascii_lowercase
ALP = string.ascii_uppercase

def atbash(ptext):
    cipher = ''
    for i in ptext:
        if i in alp:
            cipher += alp[-(alp.index(i)+1)]
        elif i in ALP:
            cipher += ALP[-(ALP.index(i)+1)]
        else:
            cipher += i
    return cipher

if __name__ == "__main__":
    plain = input("enter the string to encode: ")
    print(atbash(plain))
