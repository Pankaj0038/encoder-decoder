#!/usr/bin/python

class base85:
    def encode(flag):
        li = []
        l = []
        for i in range(0,len(flag),4):
            l.append(flag[i:i+4])
        for k in l:
            ele = 0
            for j in range(0,len(k)):
                ele = ele + (ord(k[j])<<8*(3-j))
            li.append(ele)
        enc = ''
        for num in li:
            n0 = chr(int(((num/pow(85,4)) % 85) + 33))
            n1 = chr(int(((num/pow(85,3)) % 85) + 33))
            n2 = chr(int(((num/pow(85,2)) % 85) + 33))
            n3 = chr(int(((num/pow(85,1)) % 85) + 33))
            n4 = chr(int(((num/pow(85,0)) % 85) + 33))
            key = n0 + n1 + n2 + n3 + n4
            enc += key
        print(enc)


a = input("enter the string to encode: ")
base85.encode(a)
'''b = input("enter the string to decode: ")
base85.decode(b)'''
