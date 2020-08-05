
###########################################################
#faktoriyel bulma#
def fak():
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

