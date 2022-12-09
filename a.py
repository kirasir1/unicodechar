import unicodedata
string=''
a=[*string]
for i in range(len(a)):
    a[i]=ord(a[i])
    match i%2:
        case 0:
            a[i]+=230
            if a[i]>65533:
                a[i]-=65533
        case 1:
            a[i]-=65
            if a[i]<0:
                a[i] += 65533
print(a)
for i in range(len(a)):
    a[i]=chr(a[i])
print(a)
print(''.join(a))
for i in range(len(a)):
    a[i]=ord(a[i])
    match i%2:
        case 0:
            a[i]-=230
            if a[i]>65533:
                a[i]+=65533
        case 1:
            a[i]+=65
            if a[i]<0:
                a[i] -= 65533
print(a)
for i in range(len(a)):
    a[i]=chr(a[i])
print(a)
print(''.join(a))
