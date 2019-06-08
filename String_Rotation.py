s=input('Input a string ')
q= int(input('Magnitude'))
dm=input('magnitutde with direction')
k = []
if len(s)>=1 and len(s)<=30 and q>=1 and q<=10:
    for j in range(len(dm)):
        if dm[j]=='L':
            a = s[int(dm[j+1]):]+s[:int(dm[j+1])]
            z = a[0]
            k.append(z)
        elif dm[j]=='R':
            b = a[-(int(dm[j+1])):]+a[:-(int(dm[j+1]))]
            y = b[0]
            k.append(y)
        else:
            pass
    substring=''
    for i in k:
        substring+=i
    if substring in s:
        print('YES')
    else:
        print('NO')
