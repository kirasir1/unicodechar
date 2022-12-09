string=''
key='蘆qwfqwf蘆qcwqwcfwq屢mjyrthjkl큃'
a=[*string]
def genkeyshift(keylist):
    keyvalue = 0
    keystr=[*keylist]
    for i in range(len(keystr)):
        keystr[i]=ord(keystr[i])
        match i % 2:
            case 0:
                keyvalue += keystr[i]
            case 1:
                keyvalue -= keystr[i]
    return abs(keyvalue)
def ciphertext(a, key):
    for i in range(len(a)):
        a[i]=ord(a[i])
        match i%2:
            case 0:
                a[i]+=key
                while a[i]>65535:
                    a[i]-=65535
            case 1:
                a[i]-=key
                while a[i]<0:
                    a[i]+=65535
    for i in range(len(a)):
        a[i]=chr(a[i])
    return ''.join(a)
def deciphertext(a, key):
    for i in range(len(a)):
        a[i]=ord(a[i])
        match i%2:
            case 0:
                a[i]-=key
                while a[i]<0:
                    a[i]+=65535
            case 1:
                a[i]+=key
                while a[i]>65535:
                    a[i] -= 65535
    for i in range(len(a)):
        a[i]=chr(a[i])
    return ''.join(a)
generated=genkeyshift(key)
print(generated)
txt=[*ciphertext(a, generated)]
print(txt)
print(deciphertext(txt, generated))
