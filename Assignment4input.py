print(" Question 1")

def tower(n,source,target,middle):
    if n<1:
        print("not possible")
        return
    if (n==1):                      
                                                                    
        print(f' Move disk {n} from rod {source} to rod {target}')            # disk 1 is smallest and nth disk is largest
        return
    tower(n-1,source,middle,target)
    print(f' move disk {n} from rod {source} to rod {target}')
    tower(n-1,middle,target,source)

n = int(input("enter the number of disks>>"))
tower(n,"A","B","C")   
print(" -----Done----")



print("Question 2")
from math import *

n=int(input("enter the Length of pascal triangle >> "))
print("By loop Method")
if(n<=0):
    print("Invalid entry by user")
else:
    print((n+2)*" "+' 1')              
    for row in range(n - 1):
        output = ""                    
        for column in range(row + 2):
            output = output + 2*" " + str(int(factorial(row + 1) / (factorial(column) * factorial(row + 1 - column))))     # using concept of nCr for pascal triangle

    print((n-row)*(" ") + output)

# By Recurssion ______________


def factorial(n):    # defining a function to calculate a factorial
    if n==1:

        return 1
    if n==0:
        return 1
    for i in range(1,n+1):
        return n*factorial(n-1)
def comb(m,n):                                        # defining the funtion to calculate the nCr
    res=factorial(m)//(factorial(n)*factorial(m-n))
    return res
r=int(input("Enter the length of pascal triangle>>"))
print("By Recursion")
for i in range(0,r):
    for j in range(0,i+1):

        print( comb(i,j),end=" ")
    print()




print("Question 3")


a=int(input("Enter the 1st number>>"))
b=int(input("Enter the 2nd number >>"))
quotient=a//b
remainder=a%b

# Part (a) ------------------------------------------------------------------------
print(("Part(A)"))
print("Quotient  is callable >>" ,callable(quotient))   # Checking whether quotient is callable or not
print("Remainder is callable >>" ,callable(remainder))

# part (b) -----------------------
print(("Part(B)"))

if remainder==0:
    print("Remainder is zero")
if quotient ==0:
    print("quotient is zero")
else:
    print("All values are non zero")

# part (c) ------------------------
lst=[]   # vacant list to store the value
lst1=[quotient+4, remainder + 4, quotient +5, remainder+5, quotient+6, remainder+6]
for value in lst1:
    if (value>4):
        lst.append(value)
print("Part(c)")
print("The values greater than 4 is contained in this list ",lst)

# part(D) ---------------------------

set1=set(lst)  # converting into set datatype

print("Part(D)")
print("our set is >>" ,set1)

# part(E) -----------------------------------

immutable_set = frozenset(set1)           # we use a inbuilt function " frozenset" to make set immutable
print("Part (E)")
print("Immutable set is >>",immutable_set)

# Part (E) -------------------------

print("Part(F)")
print("The required hash value of maximum valued element of set is ",hash(max(immutable_set)))


print(" Question 4 ")


class student :
    def __init__(self,name,roll_number):
        self.name= name
        self.roll_number= roll_number
    def __del__(self):                        
        print("Your object is destroyed")
        
s1 = student("ankit sharma", "21103021")    # here we create a object named as s1

print(f'Name is {s1.name} and Roll no.  is {s1.roll_number}')

del s1                # Here we are deleting our created object



print("Question (5) ")

class employees :

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

# creating the objects / employees

emp1=employees('Mehak','40000')
emp2=employees('Ashok','50000')
emp3=employees('Viren','60000')

emp1.salary='70000'         # updating the salary od Mehak
print("Part(a)")
print(f'The new salary of {emp1.name} is {emp1.salary}')

# Part(b) -----------------------------
del emp3            # here we are deleting the record of employee Viren
print("The employee record of Viren is deleted")

print("Question (6)")


def words(n):                       # defining a function to calculate all possibility of word that can be made using a word given by george
    if len(n)==1:
        return [n]
    word= words(n[1:])
    char=n[0]
    result=[]
    for i in word:
        for j in range(len(word)+1):
            result.append(i[:j] + char + i[j:])
    return result
n=str(input("George please enter a word>>"))

total_word =list(set(words(n)))
m=input("Enter the word you want to check >>")
if m in total_word:
    ask=input("Is the word is make any sense (y/n)>>")
    if ask.upper()=='Y':                                  # asking shopkeeper whether word make any sense
        print("Your friendship is true")
    else:
        print("your friendship is fake")
else:
    print("Your words letter is not matching with the word given by George")
