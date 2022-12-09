from configparser import ConfigParser
#from tkinter import filedialog
from Demo05 import *
#numb=primenum(1000)
#KEYOPEN=numb[0]+numb[1]
s = 'asdasffwfqw'
def code(s, KEYOPEN):
    pwdS=""
    for i in range(len(s)//len(str(KEYOPEN))+1):
        pwdS+=str(KEYOPEN)
    SS=""
    for i in range(len(s)):
        C=s[i]
        K=ord(C)
        Kk=K^int(pwdS[i])
        Cc=chr(Kk)
        SS+=Cc
    return SS
def decode(text, KEYOPEN):
    pwdS = ""
    for i in range(len(text) // len(str(KEYOPEN)) + 1):
        pwdS += str(KEYOPEN)
    SS = ""
    for i in range(len(text)):
        C = text[i]
        K = ord(C)
        Kk = K^int(pwdS[i])
        Cc = chr(Kk)
        SS += Cc
    return SS
def codeciph(keyopen, keyuser):
    return keyopen^keyuser

#save(text=s)