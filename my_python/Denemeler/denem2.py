n =12
sayılar=range(n)
sayılar=sayılar[:]
aa=[]

def a(sayı):
    for i in range(int(sayı)):  
        for t in range(int(sayı/3)):
            print(' ',end='')
        for j in range(i):
            print('*',end='')
            print(' ',end='')
        print('')

def b(sayı):
    for i in range(sayı):
        aa.append(int(i))
    aa.reverse()

def bb(sayı):
    for i in aa:
        print('',end='')
        print(i*'* ',end='')
        print(' ')
b(n)
bb(n)