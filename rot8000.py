#!/use/bin/python3
import string
alp = string.ascii_lowercase
ALP = string.ascii_uppercase
def encode(ptext):
    cipher = ''
    for i in ptext:
        cipher += chr(ord(i)+ 31753)
    return cipher
def decode(cipher):
    ptext = ''
    for i in cipher:
        ptext += chr(ord(i)-31753)
    return ptext

if __name__ == '__main__':
    text = input('Enter the text :')
    choice = input('Enter your choice encode(e)/decode(d)')
    if choice=='e':
        print(encode(text))
    elif choice=='d':
        print(decode(text))
    else:
        print("invalid choice")
    