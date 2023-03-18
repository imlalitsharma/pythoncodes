#!/usr/bin/env python
# coding: utf-8

# In[7]:


print("Hello world")


# In[3]:


a=5
b=5
c=b+5
print(c)


# In[4]:


#List Of Basic program
# Write a program to add two numbers
a = int(input("Enter first number:- "))
b = int(input("Enter second number:- "))
c = a+b
print("Addition is:- ",c)


# In[6]:


#Write a program to subtract two numbers
a = int(input("Enter first number:- "))
b = int(input("Enter second number:- "))
c = a-b
print("Subtraction is:- ",c)


# In[7]:


#Write a program to multiply two numbers
a = int(input("Enter first number:- "))
b = int(input("Enter second number:- "))
c = a*b
print("Mulitplication is:- ",c)


# In[11]:


#Write a program to divide two numbers
a = int(input("Enter first number:- "))
b = int(input("Enter second number:- "))
c = a/b
print("Dicision is:-",int(c))


# In[2]:


# Write a program to perform addition/subtraction/multiplication/division in the same program
a = int(input("Enter first number:- "))
b= int(input("Enter second numbr:- "))
c = a+b
print("Addition is:- ",c)

w = int(input("Enter the number:- "))
x = int(input("Enter the number:- "))
y = w-x
print("Subtraction is:- ",y)

m = int(input("Enter the number:- "))
n = int(input("Enyter the number:- "))
o = m*n
print("Multiplication is:- ",o)

g = int(input("Enter the number:- "))
h = int(input("enter the number:- "))
i = g/h
print("Division is:- ",i)




# In[6]:


#Write a program to calculate:
#Area Of Rectangle
length = 23
breadth = 12
area = length * breadth
print(area)


# In[8]:


#Perimeter Of Rectangle
length = 12
breadth = 13
perimeter = 2*(length + breadth)
print(perimeter)


# In[10]:


#Area Of Square
side = 12
area = side*side
print(area)


# In[11]:


#Perimeter of Square
side = 15
perimeter = 4 * side 
print(perimeter)


# In[14]:


#Area Of Circle
radius = 12
area = 3.14 * radius * radius
print(area)


# In[13]:


#Circumference of Circle
radius = 3
circumference = 2 * 3.14 * radius
print(circumference)


# In[3]:


#Write a program to accept elcetricity unit consumption and calculate the total price at the rate of 5rs per unit. Give a 10% discount on all over bill.
unit = int(input("Enter the unit of consumption:- "))
total = unit * 5
discount = (10/100) * total
overallbill = total - discount
print("Bill is:- ",overallbill)


# In[5]:


#5 subject marks
hindi = int(input("Enter the marks:- "))
english = int(input("Enter the marks:- "))
math = int(input("Enter the marks:- "))
sst = int(input("Enter the marks:- "))
science = int(input("Enter the marks:- "))

total = hindi + english + math + sst + science
percentage = (total/500) * 100
print("Total marks:- ",total)
print("Percentage is:- ",percentage)


# In[6]:


#swap two values
a = int(input("Enter the number:- "))
b = int(input("Enter the number:- "))
print("Before swap a:- ",a)
print("Before swap b:- ",b)
c=a
a=b
b=c

print("After swap a:- ",a)
print("After swap b:- ",b)


# In[7]:


#sale amount
total = int(input("Enter the total sale amount:- "))
profit = 5/100 * total
print("Profit at 5% is:- ",profit)


# In[14]:


from tkinter import *
import tkinter as tk
root  =  Tk()
root.title("hello")
root.geometry('1080x1080')

label = Label(root,text="hello jii").pack()
frame = Frame(root)
frame.pack()


btn = Button(root, text = 'Click me !', bd = '5',command = root.destroy)
btn.pack(side = 'top')

button = Button(frame, text = "MINIMIZE" , bd='10', command = root.minimize1)
button.pack()


root.mainloop()


# In[8]:


#write a program to print 1 to 10

i=1
while(i<=10):
    print(i)
    i=i+1


# In[13]:


#write a program to print 1 to 10

i=1
while(i<=10):
    print(i, end=" ")
    i=i+1


# In[1]:


#Write a program to print 1 to n
n=  int(input("Enter the number you want to print the numbers"))
i = 1
while(i<=n):
    print(i)
    i = i+1


# In[3]:


# Write a progam to write natural number in reverse order
i = 10
while(i>=1):
    print(i)
    i = i-1


# In[2]:


# Write a program to print n to 1

n = int(input("Enter Number:"))
i = n
while(n>=1):
    print(n)
    n = n-1


# In[3]:


# Write a program to write find sum from 1 to n.
n = int(input("Enter the number till you want to get sum:- "))
i = 1
sum = 0
while(i<=n):
    sum = sum + i
    i = i+1
print("Sum is = ",sum)


# In[8]:


# Write a program to print sum of SQUARE from 1 to n.
n = int (input("Enter No:- "))
i =1
sum  = 0
while(i<=n): 
    sum = sum + (i*i)
    i = i+1
print("SUM OF SQUARE IS:- ",sum)
    


# In[2]:


# Write pogram to print sum of cube from 1 to n.
n = int(input("Enter the number:- "))
i = 1
sum = 0
while(i<=n):
    sum  = sum + i*i*i
    i = i+1
print("SUM  OF CUBE IS:- ",sum)


# In[1]:


# Write a program to print only even number between 1 to n.
n = int(input("Enter the number:- "))
i = 2
while (i<=n):
    if i%2==0:
        print(i)
    i=i+1


# In[4]:


# Write a program to print only even number between 1 to n.
n = int(input("Enter the number:- "))
i = 2
while (i<=n):
    print(i)
    i=i+2


# In[1]:


# Write  a program to find sum of first n even numbers.
n = int(input("Enter Number:- "))
i = 1
sum = 0
count = 0

while(i<=n):
    if i%2==0:
        sum = sum+i
    i = i+1
    count = count+1     #'''Additional'''
print("Sum IS :- ",sum)
print("Count Of Numbers:- ",count)


# In[8]:


# Level 2 Questions
#1. Write a program to find the sum of digits of a given number 
i = int(input("Enter the number to find sum of digits:- "))
sum = 0
while(i>0):
    sum = sum + i%10
    i = i//10
print("Sum of digits is:- ",sum)


# In[12]:


#2.Write a program to find the sum square of digits of a given number.
i  = int(input("Enter the number to find the sum of square of digits.:- "))
sum =  0
while(i>0):
    sum = sum +(i%10)*(i%10)
    i = i//10
print("The sum of square of each digits :- ",sum)


# In[14]:


#3.Write a program to find the sum cube of digits of a given number.
i  = int(input("Enter the number to find the sum of square of digits.:- "))
sum =  0
while(i>0):
    sum = sum +(i%10)*(i%10)*(i%10)
    i = i//10
print("The sum of cube of each digits :- ",sum)
    


# In[5]:


#4.Write a program to check whether a given numberis armstrong or not.
i  = int(input("Enter the number to check armstrong:- "))
orig = i
sum =  0
while(i>0):
    sum = sum +(i %10)*(i%10)*(i%10)
    i = i//10
if(orig==sum):
    print("Yes it's armstrong")
else:
    print("No it's not armstrong")
    


# In[6]:


#5. Write a program to find the product of digits of number.
i= int(input("Enter the nummber to find the product:- "))
pro = 1
while(i>0):
    pro = pro* i%10
    i = i//10
print("Prduct is:-  ",pro)


# In[10]:


#6. Write a program to reverse a given number
i = int(input("Enter the number to reverse:- "))
rev = 0
while(i>0):
    rev = (rev * 10) + (i %10)
    i = i//10
print("Reverse of the number is:- ",rev)


# In[1]:


#7. Write a program to Check a Number is Palindrome or not.
i = int(input("Enter the number to check palindrome or not "))
orig = i

rev = 0
while(i>0):
    rev =  (rev*10) + (i%10)
    i = i//10
    
if(orig == rev):
    print("Yes it's a Palindrome ")
else:
    print("No it's not a Palindrome ")


# In[9]:


#9. Write a program to print factors of a given number.
x = int (input("Enter the Number to print factors of it:- "))
i = 1
for i in range(1,x+1):
    if(x%i==0):
        print(i)


# In[6]:


#9. Write a program to count total number of factors of a given number.
x = int (input("Enter the Number to print factors of it:- "))
i = 1
count = 0
for i in range(1,x+1):
    if(x%i==0):
        print(i)
        count = count +1
print("Total number of factors are:-  ",count)


# In[17]:


# Write a programe to check that the number is prime or not.

n = int(input("Enter the number to know it's prime or not "))
count = 0
i = 1
while(i<=n):
    if(n%i==0):
        count = count + 1
    i = i+1
if(count == 2):
    print("Prime")
else:
    print("Not Prime")


# In[2]:


# Write a program to print the factorial of a given number.

i= int(input("Enter the number "))
fact = 1
while(i>0): 
    fact  = fact  * i
    i = i-1
print("Factorial is ", fact)


# In[1]:


#Fibonacci series
n = int(input("Enter the number:- "))
a = -1
b = 1
for i in range (1,n+1):
    c = a+b
    a=b
    b=c
    i = i+1
    print(c)


# In[12]:


# for loop factorial
n = int(input("Enter the number:- "))
fact = 1
for i in range(1,n+1):
    fact = fact * i
print(fact)


# In[4]:


#8. Write a program to print fibonacci series upto given number.
n = int(input("Enter the number:- "))
a = -1
b = 1
c = 0
while(c<=n):
    print(c)
    a = b
    b = c
    c = a + b


# In[10]:


n = int(input("Enter the number"))
for i in range(1,n+1):
    print("*" *i)
 


# In[1]:


i = 1
while(i<=5):
    j = 1
    while(j<=i):
        print("*" , end = ' ')
        j = j+1
    print()
    i = i+1


# In[1]:


i  = 1
while (i<=5):
    b = 1
    while(b<=5-i):
        print(" ", end= "")
        b= b+1
    j = 1
    while(j<=i):
        print("*", end = " ")
        j = j+1
    print()
    i  =i+1


# In[4]:


#Write a prograam to print table of a given number.
n = int(input("Enter the number : "))
for i in range(1,11):
    print(n,"*",i,"=",n*i)
    i = i+1


# In[6]:


# Function
#subprogram
#fucntion is a part of a program
#it has two importants things 1.function definition 2. function calling

#Example:- 

def msg():
    print("SHURUAT")
msg()
msg()
msg() 


# In[12]:


# Program  to find addition of two numbers using function.
def add():
    a = int (input("Enter First Number "))
    b = int (input("Enter Second Number "))
    c = a+b
    print("Addition is = ",c)
    
add()


# In[17]:


#Function Arguments and Parameters.
# This is the value which iss supplied to the function to operate on .


def add(a,b):
    c = a+b
    print("Addition is = ",c)
#a = int (input("Enter First Number "))
#b = int (input("Enter Second Number "))
add(10,11)
    


# In[21]:


# write a program to check the number is odd or even.
def oddeve():
    x = int(input("Enter the number to check:- "))
    if(x%2==0):
        print("Number is even")
    else:
        print("Number is odd")
oddeve()


# In[24]:


#With Arguments.
def oddeve(x):
    if(x%2==0):
        print("Number is even")
    else:
        print("Number is odd")
x = int(input("Enter the number to check:- "))
oddeve(x)


# In[25]:


#1. No argument no return
#2. With argument no return
#3. No argument with return
#4. With argument with return


# In[28]:


#1. No argument no return
def add():
    a = int(input("Enter First Number"))
    b = int (input("Enter second number"))
    c = a+b
    print("Sum=",c)
add()


# In[31]:


#2. With argument no return
def add(a,b):
    c = a+b
    print("Addition is= ",c)
a= int(input("Enter first number"))
b = int(input("Enter second Number"))
add(a,b)


# In[32]:


#3. No argument with return
def add():
    a = int(input("Enter First Number"))
    b = int (input("Enter second number"))
    c = a+b
    return c
x = add()
print("Addition is = ",x)


# In[33]:


#4. With argument with return
def add(a,b):
    c = a+b
    return c
    
a= int(input("Enter first number"))
b = int(input("Enter second Number"))
z = add(a,b)
print("Addition is = ",z)


# In[1]:


#Defualt Arguments
def add(a,b,c=5):
    d = a+b+c
    print(d)
add(5,6)
     


# In[8]:


#Break and continue statement.
for i in range(1,6):
    if(i==2):
        break
    print(i)


# In[5]:


for i in range(1,6):
    if(i==2):
        continue
    print(i)


# In[10]:


#String in python are stored as individual characteres i. e. indexed wise. The index by default starts with 0.
#1. Forward Indexing
#2. Backward Indexing
#string are immutable and hence you cannot change the 
#individual letters of string using assignment oprator.


name = "Shyam"
print(name)


# In[22]:


name = "Shyam"
for i in name:
    print(i,end="  ")
   


# In[23]:


#string Operators


# In[27]:


a = "Hello World"
print(a[6:10])
print(a[:6])
print(a[6:])
print(a[2:-2])


# In[4]:


#Concatenation
a  = "hello"  + " hii"

print(a)


# In[6]:


i = int(input("Enter the name"))
rev = 0
while i>0:
    rev  = (rev * 10) +  (i%10)
    i = i//10
print("reverse number", rev)


# In[1]:


d = int(input("Enter the Number"))
sum = 0
while d > 0:
    sum = sum + d%10
    d  = d//10
print(sum)


# In[8]:


d = int(input("Enter the Number"))
rev = 0
while (d>0):
    rev = (rev * 10) + (d % 10)
    d  = d//10
print(rev)


# In[5]:


#6. Write a program to reverse a given number
i = int(input("Enter the number to reverse:- "))
rev = 0
while(i>0):
    rev = (rev * 10) + (i %10)
    i = i//10
print("Reverse of the number is:- ",rev)


# In[ ]:


i = 1
k = 1
while i<=5:
    b=1 
    while b<=5-i:
        print(" ", end=" ")
    j =1
    while j<=k:
        print("*",end=" ")
    k = k+2
print()
i = i+1
    
        


# In[3]:


a = input("Enter a string ")
vowel = 0
cons = 0
for i in range (0,len(a)):
    if a[i]!=" ":
        if a[i]=="a" or a[i]=="e" or a[i]=="i" or a[i]=="o" or a[i]=="u" or a[i]=="A" or a[i]=="E" or a[i]=="I" or a[i]=="O" or a[i]=="U":
            vowel+=1
        else:
            cons+=1
print("Total Vowels:-",vowel)
print("Total Consonants:-",cons)

     


# In[9]:


a = "123aaa"
print (a.isdigit())
print (a.isalnum())
print (a.isspace())


# In[ ]:





# List is a collection of different types of values.
# differnce betweeen list and array
# :-different tyopes of data can store
# [a,b]

# In[10]:


a=[]
x= input().split()
a.append(x)
print(a)

for i in range (len(a)):
    x[i] = int(x[i])
    
print("Sum is",sum(x))


# In[7]:


#python program to find the sum of elements of the list.


n = input()
d = n.split()
for i in range(len(d)):
    d[i]  = int(d[i])
print("Sum is ",sum(d))


# In[13]:


#python program to count the odd and even numbers in the list.


n = input()
d = n.split()
even = 0
odd = 0
for i in range(len(d)):
    d[i]  = int(d[i])
    if d[i]%2==0:
        even+=1
    else:
        odd+=1
        
print("Even Numbers:-",even)
print("Odd Numbers:-",odd)


# In[5]:


#program to find the sum of even numbers and product of odd numbers
#python program to count the odd and even numbers in the list.


n = input()
d = n.split()
sum = 0
pro = 1
for i in range(len(d)):
    d[i]  = int(d[i])
    if d[i]%2==0:
        sum +=d[i]
        
    else:
        pro*=d[i]
        
print("sum",sum)
print("product",pro)


# In[2]:


n = input()
d = n.split()
sum = 0
pro = 1
for i in range(len(d)):
    d[i]  = int(d[i])
    x=d.count(12)
print(x)


# In[2]:


a = [ ]
size = int(input("Enter size"))
for i in range(size):
    val = int(input("Enter values "))
    a.append(val)
key = int(input("Enter the number to be count"))
count = 0
for i in range(size):
    if a[i] == key:
        count+=1
print("Frequency= ",count)


# In[3]:


a = [ ]
size = int(input("Enter size"))
for i in range(size):
    val = int(input("Enter values "))
    a.append(val)
max=a[0]
for i in range(size):
    if a[i] >max:
        max = a[i]
print("Maximum ",max)


# In[7]:


a = [ ]
size = int(input("Enter size"))
for i in range(size):
    val = int(input("Enter values "))
    a.append(val)
i = 0 
j =size-1
while i<j:
    t = a[i]
    a[i]=a[j]
    a[j]=t
    i = i+1
    j = j-1
    print("List after reverse=")
    for i in range(size):
        print(a[i])


# In[ ]:


n = int(input())
arr = map(int, input().split())
maxval = max(arr)
print(maxval)


# In[2]:


T = int(input())
for _ in range(T):
    X,Y = map(int,input().split())
    z = lambda x,y: print(y-x) if y-x>0 
    print(z)


# List is ordered and mutable. List allow duplicates.
# Tuple is ordered and unchangeable.
# ()
# different types of elements.
# List Occupies more memory space as compared to tuple.
# List takes more time to execute as compared to tuples.

# In[1]:


import sys
list1 = [1,2,"ram"]
tuple1 = (1,2,"ram")
print(sys.getsizeof(tuple1))
print(sys.getsizeof(list1))


# In[4]:


import timeit
listtime = timeit.timeit(stmt ="[1,2,3,4,5]",number =10000000)
tupletime = timeit.timeit(stmt = "(1,2,3,4,5)",number =10000000 )
print("list",listtime)
print("tuple",tupletime)


# In[7]:


#Declaration of tuple
tuple1 = ()    #empty tuple

t1 = (1,)
type(t1)


# In[8]:


list = [1,2,3,4,5]
tuple1 = tuple(list)
print(tuple1)


# In[10]:


t1 = tuple("world")
t1


# In[15]:


#travesring tuple
tuple1 = (1,2,3,4)
for t in tuple1:
    print (t)
print("$$$$$$$$$$$$$$$$")
for i in range(len(tuple1)):
    print(tuple1[i])


# In[17]:


tuple1+tuple1


# In[19]:


#repeating
tuple1 = (1,2,3)
tuple2 = tuple1*3
tuple2


# In[23]:


#T=[start:stop:step]
t = (1,2,3,4,5,6,7)
print(t[2:5])


# In[2]:


t = (1,2,3,4,5,6,7)
print(len(t))
print("-------------------------------------------------------")    
print(min(t))
print("-------------------------------------------------------")    
print(t.index(2))
print("-------------------------------------------------------")    
print(t.count(1))
print("-------------------------------------------------------")    
""""tuple() is used as a constructor which is used to create tuples
from different types of values."""
print    
#creating tuple from key of dictionary
tuple1 = tuple({1:"m",2:"n",3:"f"})
print(tuple1)


# In[38]:


#Change tuple values
#tuples are immutabble but there is a way to achieve this 
#tuple to list then change values then again make it tuple.


xtuple = (1,2,"apple","banana","cherry")
y = list(xtuple)
y[1] = "kiwi"
x  = tuple(y)
print(x)


# In[41]:


#for checking
tuple = ("ram","shyam")
x = input("Enter the value to be search")
if x in tuple:
    print("yes")
else:
    print("no")


# In[42]:


#we cannot add items in tuple\
#to delete items entirely cannot possible
#entire tuple can be deleted using del


# In[3]:


#dictionary is a collection which is unordered and changeable
dict = {"brand":"Suzuki", "model":"Dzire","year":2020}
print(dict["brand"])
print(dict.get("model"))
print("-------------------------------------------------------")    
#x denotes keys

for x in dict:
    print(x)
print("-------------------------------------------------------")    
for x in dict:
    print(dict[x])
    
dict['color']='WHITE'
print(dict)
    


# In[7]:


#popitem()
#last item deleted
#pop("keyname")
#clear__elements will be cleared become empty
#del dict['keyname']


"""the fromkeys() method returns a dictionary with the specified keys and the specified value"""
x = ('firstkey','secondkey','thirdkey')
y = (0)
dict2 = dict.fromkeys(x,y)
print(dict2)
dict3 = dict2.copy()
print(dict3)


# In[13]:



x = ('firstkey','secondkey','thirdkey')
y = (0)
dict2 = dict.fromkeys(x,y)
print(dict2)
dict3 = dict2.copy()
print(dict3)
z = dict2.setdefault("place","New Delhi")
print(dict2)
dict2.update("color","white")
print(dict2)


# In[14]:


dict = {"brand":"Suzuki", "model":"Dzire","year":2020}
dict.update("color","white")
print(dict)


# In[6]:


st ={}
while True:
    line = input("Please input the ID and name seperated by comma or q to exit")
    if line == 'q':
        break
    id,name = line.split(',')
    st.update({id:name})
    
for x,y in st.items():
    print(x,y)
key = input("Enter id to be search:")
if key in st:
    print('key=',key,'value',st[key])
else:
    print("Key not found:")


# In[22]:


n = int(input())
for i in range(n):
    print(" ")
    for k in range (5-i):
        print("*",end=" ")
print()


# In[8]:


#filter

ages  = [13,14,15,20,23,24]
def myfun(x):
    if x<18:
        return False
    else:
        return True

def myfun1(y):
     return y*y
adults = list(filter(myfun,ages)) 
print(adults)
squares =  list(map(myfun1,adults))
print(squares)



# In[4]:


from functools import reduce
def myfunc(a,b):
    return a+b

val = [1,2,3,4,5]
add = reduce(myfunc,val)
print("Addition",add)


# In[6]:


l = []
size = int(input())
for _ in range (size):
    val = int(input())
    l.append(val)
print(len(l))
print(Max (l))
print(Min(l))
#print(cmp(l1,l2))
obj = 13
print(l.append(obj))
print(l.index(2))
print(l.insert(1,23))
print(l.remove(5))
print(l.reverse())
print(l.sort())
print(l.pop())


# In[ ]:




