#add sub multi and divide
'''a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=a+b
print("addition of a and b is :",c)
d=a-b
print("subtraction of a and b is :",d)
e=a/b
print("division of a and b is :",e)
f=a%b
print("modulas of a and b is :",f)
g=a*b
print("multipication of a and b is :",g)
h=a//b
print("floor division of a and b is :",h)'''
#name and age
'''a=input("enter your name :")
print("your name is",a.upper())
b=int(input("enter your age:"))
print(f"you are {b} years old")'''
#even and odd number
'''a=int(input("enter the number:"))
if a%2==0:
    print("the given number is even ")
else:
    print("the given number is an odd number")'''
#password
'''a="sam@1983"
b=input("enter the password:")
if b==a:
    print("       WELCOME       ")
else:
    print("incorrect password")'''
#positive number negative number and zero
'''a=float(input("enter the number:"))
if a<0:
    print("it is an negative number")
elif a>0:
    print("it is an positive number")
else:
    print("the given number is zero")'''
#divisible by 3 and 7
'''a=int(input("enter the number:"))
if a%3==0 and a%7==0:
    print("it is divisible by both 3 and 7")
elif a%3==0:
    print("it is divisible by 3")
elif a%7==0:
    print("it is divisible by 7")
else:
    print("it is not divisible by 3 and 7")'''
#bill
'''print("     MENU CARD     \n1.Tea=10\n2.Puri=15\n3.Vada=5\n4.Idly=10")
trate=10
prate=30
vrate=5
irate=10
tea=int(input("enter the number of tea you have ordered:"))
puri=int(input("enter the number of puri you have ordered:"))
vada=int(input("enter the number of vada you have ordered:"))
idly=int(input("enter the number of idly you have ordered:"))
t=tea*10
p=puri*15
i=idly*10
v=vada*5
total=t+v+i+p
print("total cost=",total)
gst=total*10/100
print("price after adding 10% gst:",gst+total)'''
#user id and password
'''userid="samthegreat"
password="sam123"
a=input("enter the userid:")
b=input("enter the password:")
if a==userid and b==password:
    print("   WELCOME   ")
elif a==userid and b!=password:
    print("userid is correct but the password is wrong")
elif a!=userid and b==password:
    print("userid is wrong but the password is correct")
else:
    print("both are wrong")'''
#all arithematic operations
'''a=int(input("enter the first number:"))
b=int(input("enter the second:"))
c=input("enter the operator:")
if c=='+':
    print("a+b=",a+b)
elif c=='-':
    print("a-b=",a-b)
elif c=='/':
    print("a/b=",a/b)
elif c=='*':
    print("a*b=",a*b)
elif c=='//':
    print("a//b=",a//b)
else:
    print("please enter the correct operator")'''
#even next to odd
'''
for i in range(41):
    if i%2==0:
        print(i,end=' ')    
    else:
        print(i)'''
#list
'''l=[10,20,30,50,25,80]
print(l)
n=int(input("enter the element you want to remove:"))
if n in l:
    l.remove(n)
    print("list after removing the element:",l)
else:
    print("element not found")
    l.append(n)
    print("list after adding the element:",l)'''
#addition of two numbers using loop
'''a=input("do you want to add:")
while a=="yes" or a=="YES":
    b=int(input("enter the first number:"))
    d=int(input("enter the second number: "))
    f=b+d
    print("answer:",f)
    a=input("do you want to add again:")
print("thank you ")'''
#list library
'''
l=["sam","the","great","bankai"]
while True:
    print("what operation do you want to do\n1.show all the books\n2.barrow an book\n3.return\n4.exit")
    op=int(input("enter the option:"))
    if op==1:
        print("THE BOOKS PRESENT IN THE LIBRARY ARE:")
        for i in l:
            print(i)
    elif op==2:
        c=input("enter the book you want to barrow:")
        if c in l:
            print("you have borrowed the book")
            l.remove(c)
            print("list after removing the book:",l)
        else:
            print("the book does not exist in our library")
    elif op==3:
        d=input("enter the book you want to return:")
        if d in l:
            print("the book already exists in the library")
        else:
            l.append(d)
            print("list after adding the returned book:",l)
    else:
        print("thank you for visiting the library")
        break'''
#tuple
#type casting
'''a=(1,2)
b=list(a)
print(type(b))
b.append(12)
c=tuple(b)
print(type(c))
print(c)'''
#set
'''s{True,1,0,False,"sam"}
print(s)
s.add("britto")#to add an element
s.remove("britto")#to remove an element 
print(s)
s.pop()#removes random element in list it removes the last element
#dictionary
d={"name":"sam","age":18,"city":"ooty"}#key + value=items
print(d)
d["age"]=50#update (change) if not present it adds the item
print(d)
a=dict(name="sam",age=18,gender="male")
print(a)
for i,j in d.items():#d.keys()for key nad d.values()for value
    print(i)'''
#MONEY WITHDRAW
'''a=0
f=50000
print("amount available in your account is :",f)
while a<=3:
    a+=1
    b=int(input("enter the amount you want to withdraw:"))
    if b<=f:
        f-=b
        print("account balance:",f)
        if f==0:
            print("THANKYOU FOR BANKING WITH US")
            break
    else:
        if b>f:
            print("INVALID AMOUNT")
            continue'''

#otp generation
'''import random 
a=int(input("enter the number of digits to get your otp:"))
for i in range(a):
    b=random.randint(1,9)
    print(b,end='')'''
    
#random number game(guess the number)
'''import random
a=0
b=random.randint(0,9)
while True:
    a+=1
    c=int(input("enter an single digit number:"))
    if c==b:
        print("you guessed it right you win")
        break
    else:
        print("you loose try again")
        continue
print("number of attempts=",a) '''
#stone, paper ,scissor game
'''import random
l=["stone","paper","scissor"]
while True:
    a=random.choice(l)
    b=input("enter stone ,paper,or scissor:")
    if a=="stone" and b=="stone":
        print("try again")
        print("the system choice was :",a)
    elif a=="stone" and b=="paper":
        print("you win")
        print("the system choice was :",a)
    elif a=="stone" and b=="scissor":
        print("you loose")
        print("the system choice was :",a)
    elif a=="paper" and b=="paper":
        print("try again")
        print("the system choice was :",a)
    elif a=="paper" and b=="stone":
        print("you loose")
        print("the system choice was :",a)
    elif a=="paper" and b=="scissor":
        print("you win")
        print("the system choice was :",a)
    elif a=="scissor" and b=="paper":
        print("you loose")
        print("the system choice was :",a)
    elif a=="scissor" and b=="stone":
        print("you win")
        print("the system choice was :",a)
    elif a=="scissor" and b=="scissor":
        print("try again")
        print("the system choice was :",a)
    elif b=="exit":
        print("thankyou")
        break
    else:
       print("please enter correct choice")
       continue'''
#calendar program
'''import calendar as cl
y=int(input("enter the year:"))
m=int(input("enter the month:"))
print(cl.month(y,m))
#date and time
import datetime as dt
a=dt.datetime.now()
print(a)'''
#oops concept
'''#class
class cse:
    def it():
        print("hello world")
class eee:
    def it():
        print("welcome")
ob=cse
ob.it()
oj=eee
oj.it()
#single inheritance
class father:
    def house():
        print("own house")
class son(father):
    def bike():
    print("own bike")
ob=son
ob.bike()
ob.house()
# multilevel inheritance
class father:
    def house():
        print("own house")
class mother(father):
    def cook():
        print("own car")
class son(mother):
    def bike():
    print("own bike")
ob=son
ob.bike()
ob.house()
ob.cook()
#multiple  inheritance 
class father:
    def house():
        print("own house")
    def car():
        print("the car in bangulore")
class mother:
    def cook():
        print("own car")
    def car():
        print("the car in chenai")
class son(father,mother):
    def bike():
    print("own bike")
ob=son
ob.bike()
ob.house()
ob.cook()
od.car()'''
'''# hierarchical inheritance :
class father:
    def house():
        print("own house")
    def car():
        print("the car in bangulore")
class son1(father):
    def car():
        print("own car")
    def bike():
        print("the bike in chenai")
class son2(father):
    def bike():
        print("own bike")
    def cook():
        print("son 2 cooks well")
ob=son1
ob.bike()
ob.house()
ob.cook()
od.car()
'''
#self
'''class home:
    def sum(a,b):
        print(a+b)
    def sun(c,d):
        print(c-d)
ob=home
ob.sum(2,3)
ob.sun(3,2)'''
#using self
'''class home:
    def sum(self):
        self.a="ram"
    def sun(self):
        print("name is ",self.a)#anything can be given in place of self
ob=home()
ob.sum()
ob.sun()
#function overriding to access the function from the upper class using an seperate functio and super()
class emp:
    def work(self):
        self.hrs=50
    def show(self):
        print("work hrs is ",self.hrs)
class traine(emp):
    def work(self):
        self.hrs=80
    def rst(self):# reate an seperate function to access the work
        super().work()#in the upper function
        
ob=emp()
ob.work()
ob.show()
oj=traine()
oj.work()
oj.show()
oj.rst()
oj.show()'''
#bank account
'''import random
l=[]
m=1000
z=0
while True:
    print("1.account creation\n2.deposit\n3.withdraw\n4.balance\n5.exit")
    op=int(input("enter the option :"))
    if op==1:
        a=input("enter your name:")
        b=int(input("enter your age:"))
        c=input("enter your address:")
        d=input("have you payed the initial amount:").lower()
        if d=="yes":
            f=random.randint(10000000000,99999999999)
            print( "your account number is:",f)
            l.append(f)
            print("THANKYOU FOR USING OUR BANKING SERVICE")
        else:
            print("please pay the initial amount")
    elif op==2:
        g=int(input("enter the account number:"))
        if g in l:
            print("access granted")
            h=int(input("enter the amount you want to deposit:"))
            z=m+h
            print("your amount has been deposited in your account")
            print("THANKYOU FOR USING OUR BANKING SERVICE")
        else: 
           print(" please enter the correct account number")
    elif op==3:
        e=int(input("enter the accoun number:"))
        if e in l:
            print("access granted")
            i=int(input("enter the amount you want to withdraw:"))
            z=z-i
            print("your amount has been withdrawed from your account")
            print("THANKYOU FOR USING OUR BANKING SERVICE")
        else: 
            print(" please enter the correct account number")
    elif op==4:
         j=int(input("enter the accoun number:"))
         if j in l:
            print("access granted")
            print("your current account balance is:",z)
            print("THANKYOU FOR USING OUR BANKING SERVICE")
         else:
             print(" please enter the correct account number")
    elif op==5:
        print("THANKYOU FOR USING OUR BANKING SERVICE")
        break
    else:
        print("enter the corret option")
        continue'''
#file creation
import os
x=input("enter the file name with extention:")
f=open(f"{x}","w+")
while True:
    b=input("enter the mode w or r or remove if you want to delete the file:")
    if b=="w":
        c=input("enter what do you want to write in the file:")
        f.write(c)
        f.close()
    elif b=="r":
        f=open(f"{x}","r")
        e=f.read()
        print(e)
        f.close()
        break
    elif b=="remove":
        os.remove(x)
        print("the file is removed")
        break
    else:
        print("enter the correct mode")






























































    

    


        


























 












































































































































































































































































































































































































































































































































































































































































































































































































































        
        
        
    


    




    





