#Assignment - 12 Full Stack Web Development using Python MySirG More on loops
#1. Write a python script to reverse a number.
#1st method
a=int(input("Enter a  integer number"))
b=str(a)
i=''
for e in b:
    i=e+i
print(int(i))
#2nd method
a=int(input("Enter a  integer number"))
b=str(a)
for e in range((len(b)-1),-1,-1):
    print(int(b[e]),end=" ")
#3rd method
a=int(input("\nEnter a  integer number"))
rev=0
while (a>0):
    rev=(rev*10)+a%10
    a=a//10
print(rev)    
#2. Write a python script to check whether a given number is Prime or not
a=int(input("Enter a  number="))
i=2
while i<=a-1:
    if a%i==0 :
        i=i+1
        print("non prime number")
        break
    else:
       print("prime number")
       break     
#3. Write a python script to print all Prime numbers under 100
a=1
for x in range(1,100+1):
    c=0
    for y in range(2,x):
        if x%y==0:
            c=True#or write c=1
            #print(c)  
            break
    if c==False:#write if c ==0:
        print(x)
#4. Write a python script to print all Prime numbers between two given numbers (both values inclusive)
a=int(input("Enter a number"))
b=int(input("Enter a number"))
for x in range(a+1,b+1):
    c=0
    for y in range(2,x):
        if x%y==0:
            c=True 
            break
    if c==False:
        print(x)
#5. Write a python script to find next prime number of a given number
a=int(input("Enter a number"))
while True:
    a=a+1
    for x in range(2,a):
        c=0
        if a%x==0:
            c=True 
            break
    if c==False:
        print("Next prime number is=",a) 
        break

#6. Write a python script to print first N prime numbers
def prime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True
def primegenerator(n):
    num=2
    while n:
        if prime(num):
            yield num
            n-=1
        num+=1
    return
a=primegenerator(int(input("Enter how many first n prime number you want to print=")))
for e in a:
    print(e,end=" ")            
#7. Write a python script to check whether a given pair of numbers are co-Prime numbers or not.
num1=int(input("\nEnter a number"))
num2=int(input("Enter a number"))
if num1>num2:
    for e in range(num1,0,-1):
        if num1%e==0 and num2%e==0:
            break
    if e==1:
        print("Given pair of numbers are co-Prime numbers")
    else:
        print("Given pair of numbers are not co-Prime numbers")
if num2>=num1:
    for i in range(num2,0,-1):
        if num1%i==0 and num2%i==0:
            break
    if i==1:
        print("Given pair of numbers are co-Prime numbers")
                
    else:
        print("Given pair of numbers are not co-Prime numbers")
 
#8. Write a python script to print first N terms of a Fibonacci series    
a=int(input("Enter a number"))
b,c,sum=1,0,0
for e in range(a):
    print(sum)
    c=b
    b=sum
    sum=b+c
#9. Write a python script to calculate LCM of two numbers
a=int(input("Enter a number")) 
b=int(input("Enter a number")) 
i=a*b
c=0
#print(i)
for e in range(2,i):
    if e%a==0 and e%b==0:
        print("LCM=",e)
        break
#10. Write a python script to calculate HCF of two numbers
a=int(input("Enter a number")) 
b=int(input("Enter a number")) 
if a>b:
    for e in range(a,0,-1):
        if a%e==0 and b%e==0:  
            print("HCF=",e) 
            break            
if b>=a:
    for e in range(b,0,-1):
        if a%e==0 and b%e==0:  
            print("HCF=",e) 
            break            
                    