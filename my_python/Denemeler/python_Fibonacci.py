<<<<<<< HEAD:my_python/python_Fibonacci.py
def fib(n):
    a, b = 0, 1
    while a < n:
         print(a, end=' ')
         a, b = b, a+b
    print()
##fib(4182)


def fibo(a):
    sayi1,sayi2,toplam=0,1,0
    sira =""
    for a in range(20):
         sira+=str(toplam)+" "
         sayi1,sayi2=sayi2,toplam
         toplam=sayi1+sayi2
         a+=1
    print(sira)
#fibo(0)






=======
def fib(n):
    a, b = 0, 1
    while a < n:
         print(a, end=' ')
         a, b = b, a+b
    print()
##fib(4182)


def fibo(a):
    sayi1,sayi2,toplam=0,1,0
    sira =""
    for a in range(20):
         sira+=str(toplam)+" "
         sayi1,sayi2=sayi2,toplam
         toplam=sayi1+sayi2
         a+=1
    print(sira)
#fibo(0)






>>>>>>> 5ce6d847a47dc081025733ea919b475ae0d7ec0f:python_Fibonacci.py
