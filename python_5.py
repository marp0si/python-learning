#object oriented programming
#class:
class Person:
    #-pass
    #attributes
        
        #class attributes
        address='no located'
        #constructor(yapıcı metod)
        def __init__(self,name,year):
            self.names=name
            self.years=year
            print('init calıştı')
            
        #object attributes
        
       
      
    #method

#object

p1=Person('asd',20)
p2=Person('dsa',10)

#print(p1)
#print(type(p1))
print('name:'+p1.names+'  year:'+str(p1.years))
print('name:'+p2.names+'  year:'+str(p2.years))

print(p1.address)
p1.address='aaabbbccc'
print(p1.address)















'''
class Person:
    personel=[]
    n=0
    name,surname,age
    def personadd(name, surname,age):
        personel_info=[]
        global n
        global personel
        personel_info[name,soyisim,age]
        personel[n]=personel_info
        n+=1

p1=Person('sinan','bilgili','20')

print(list(personadd))
        
   '''
    


    
