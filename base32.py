#!/usr/bin/python

class base32:
    def encode(flag):
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
        enc = ''
        binary_string=''
        for char in flag:
            binary_string += "{0:08b}".format(ord(char))
        chunks = [binary_string[i:i+5] for i in range(0,len(binary_string),5)]
        if len(chunks[-1]) < 5:
            x = 5 - len(chunks[-1])
            chunks[-1] = "{0:05b}".format(int(chunks[-1],2) << x)
        encoded_string = ''
        for i in chunks:
            encoded_string  += alpha[int(i,2)]
        print(encoded_string)


    def decode(enc):
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
        flag=''
        binary = ''
        li=[]
        for ind in range(len(enc)):
            for i in range(len(alpha)):
                if enc[ind] == alpha[i]:
                    li.append(str(i))
        for num in li:
            binary += "{0:05b}".format(int(num))
        chunks = [binary[i:i+8] for i in range(0,len(binary),8)]
        for i in chunks:
            flag += chr(int(i,2))
        print(flag)


choice = int(input('''(1) encode\n(2) decode\nEnter your choice(1 or 2): 
      '''))
if choice == 1:
    a = input("Enter you string to encode: ")
    base32.encode(a)
elif choice == 2:
    a = input("Enter your string to decode: ")
    base32.decode(a)
else:
    print("Invalid choice")
