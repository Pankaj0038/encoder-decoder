#!/usr/bin/python

li = []
for i in range(33,127):
    li.append(chr(i))

flag = input("Enter the string to encode or decode : ")
enc = ''
for char in flag:
    enc += li[((ord(char)-33)+47)%94]
print(enc)
