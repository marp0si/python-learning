sayi1,sayi2,sayi3,enbuyuk=10,20,5,0
if sayi1>=sayi2 and sayi1>=sayi3:
    enbuyuk=sayi1
elif sayi2>=sayi1 and sayi2>=sayi3:
    enbuyuk=sayi2
else :
    enbuyuk=sayi3
 
#print(enbuyuk)
###########################################################
#faktoriyel bulma#
sayi=int(input("sayi girin: "))
fak=1
if sayi==0:
    print(1) 
elif sayi<0:
    print("eksi sayilarin faktoriyeli yoktur")
else : 
    for faksay in range(1,sayi+1):
        fak=faksay*fak
    print(fak)

    
