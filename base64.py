#!/usr/bin/python

class base64:
    '''def greet(fx):
        def mfx(**kwargs):
            print("Hello, I am Gumnami , nice to see you here using my tool :)")
            fx(*args,**kwargs)
            print("thanks for appreciating me!,have a good day")
        return mfx'''
    
    #@greet
    def encode(flag):
        char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
        enc=''
        binary_string =''
        for letter in flag:
            binary_string += "{0:08b}".format(ord(letter))
        print(binary_string)
        chunks = [binary_string[i:i+6] for i in range(0,len(binary_string),6)]
        for i in range(len(chunks)):
            if len(chunks[i]) < 6:
                print(len(chunks[i]))
                x = 6 - len(chunks[i])
                print(x)
                chunks[i] = "{0:06b}".format(int(chunks[i],2) << x)
        print(chunks)
        encoded_string = ''
        for i in chunks:
            encoded_string += char[int(i,2)]
        print(encoded_string)
    
    #@greet
    def decode(enc):
        char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
        li = []
        for i in range(0,len(enc)):
            for j in range(0,len(char)):
                if enc[i] == char[j]:
                    li.append(str(j))
        print(li)
        binary = ''
        flag =''
        for num in li:
            binary += "{0:06b}".format(int(num))
        print(binary)
        chunks = [binary[i:i+8] for i in range(0,len(binary),8)]
        print(chunks)
        for i in chunks:
            flag += chr(int(i,2))
        print(flag)



a = int(input("Enter your choice encode=1/decode=2): "))

match a:
    case 1:
        flag_to_encode = str(input("Enter the string to encode: "))
        base64.encode(flag_to_encode)

    case 2:
        enc_to_decode = str(input("Enter the string to decode: "))
        base64.decode(enc_to_decode)

    case _:
        print("enter a correct choice!")

