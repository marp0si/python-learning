##my_list=[1,2,3]
##my_list=["bir",2,True,5.2]
##print(my_list)

list1=["one",10,"there"]
list2=["four",20,"six"]
list4=[list1,list2]
#print(list1+list2)
T_sayi=len(list1)+len(list2)
#print(T_sayi)
list3=[list1[0]+list2[0],list1[1]+list2[1]]
##print(list3)
##print(list4[0])
##print(list4[0][2])
##print(list4[0][2][0:4])
##################
tuple1=("asd","asd","asd")#sabit dizi
set1={"asd3":4,"asd2":2,"asd1":1}#key:value
set1 = {"apple":1, "banana":2, "cherry":3}
#print(set1["apple"])#1

#print(type(tuple1))
#print(set1["asd2"])
numbers=[1,2,3,4,5,6,7,8,9,10,5]
letters=["a","b","c","d","e","a"]
ref=max(numbers)
ref=min(numbers)
ref=max(letters)
##print(ref)
ref=min(letters)
##print(ref)
ref=numbers[::-1]
ref=numbers[:4]

numbers.insert(3,78)##3.index'e 78i ekler sonrakileri +1indexlerine atar
numbers.sort() ##diziyi k-->b siralar
numbers.reverse() ## diziyi cevirir
numbers.append(40)##dizinin sonuna 40 elemanini ekler
numbers.pop(3)##default son elemani, icindekise, indexsi siler
numbers.remove(40)## icine yazilan degeri arar ve siler

sayi=numbers.count(5)##icindeki eleman dizide kac tane var 
index=letters.index("b")#icindeki elemanin indexini verir
result="b" in letters #lettersda a elemani var mi 
numbers *=0
#print(numbers)


#asd=raw_input('marka girin= ')
#markalar=[]
#markalar.append("marka")
#print(asd)
##print(ref)
