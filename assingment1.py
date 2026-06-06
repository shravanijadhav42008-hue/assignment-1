#conditional statement

#positive negative number

a = 2

if a >= 0:
    print("positive")
else:
    print("negative")
        
        
#even odd number
    
num = 90

if num % 2 ==0:
    print("even")
else:
    print("odd")


#greater no betwen 2 number

a = 80
b = 34

if a >= b:
    print("a is greater")
else:
    print("b is greater")


#eligible to vote

age = 19

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible")
    

#divisible by 5

num = 60

if num % 5 == 0:
    print("divisible by 5")
else:
    print("Does not divisible by 5")
  
    
#Year is Leap or not
   
year = int(input("Enter year"))

if year % 4 == 0:
    print("Year is Leap ")
else:
    print("year is not leap")
    

#vowel or consonant

ch = input("Enter character")

if ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
    print("It is vowels")
else:
    print("It is consonant")
    

#greater betwen 3 numbers

a = int(input("Enter number:"))
b = int(input("Enter number:"))
c = int(input("Enter number:"))

if a >= b and a >= c:
    print("a is greater")
elif b >= b and b >= c:
    print("b is greater")
else:
    print("c is greater")


#grades

marks = int(input("Enter Marks:"))

if marks >= 90:
    print("Grade A")
elif marks >=75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
    
    
#range of 1 to 100

number = int(input("enter the number"))

if 1 <= number <= 100:
    print("number is in  range")
else:
    print("number is not in range")
    
    

#For loop

#1 to 10 using for loop

for i in range(1,11):
    print(i)


#10 to 1 reverse using for loop

for i in range(10, 0,-1):
    print(i)


#even number bet 1 to 20

for i in range(2,20,2):
    print(i)
    

#odd number bet 1 to 20

for i in range(1,20,2):
    print(i)
    
    

#sum of numbers 1 to 100

total = 0

for i in range(1,101):
    total += i
    
print("Sum=",total)



#multiplication table of given number

num=int(input("Enter a number:"))

for i in range(1,21):
    print(num,"x",i,"=",num*i)
    
    
    
#print pattern

for i in range(6):
    for j in range(i):
        print("*",end=" ")
    print()
    
    
#print each character of a string using a for loop

text = input("Enter a String:")

for ch in text:
    print(ch)
    
    
#factorial of a given number using a for loop

num = int(input("Enter a number:"))
fact = 1

for i in range(1,num+1):
    fact*=1
    
print("Factorial=",fact)



#print pattern

for i in range(6):
    for j in range(i):
        print("*",end="")
    print()
    
    

#python while loop

#1 to 10 using a while loop

a = 1

while a < 11:
    print(a)
    
    a += 1
    

#10 to 1 reverse using a while loop

a = 10
while a >= 1:
    print(a)
    
    a -= 1
    

#print even number betwen 1 to 20

i = 2

while i <= 20:
    print(i)
    i += 2
    
    

#print odd number betwen 1 to 20

i = 1

while i <= 20:
    print(i)
    i += 2



#sum of numbers from 1 to 100 using a while loop

i = 1
sum = 0

while i <= 100:
    sum += i
    i += 1
    
print("Sum=",sum)


#multiplication table of given number

num = int(input("Enter  number:"))
i = 1

while i <= 10:
    print(num,"x",i,"=",num*i)
    i += 1
    
    
#count the number of digits

num = int(input("Enter a number"))
count = 0

while num > 0:
    count += 1
    num //=10
    
print("Number of digits=",count)


#reverse a given number


num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Reversed number =", reverse)


#factorial of number


num = int(input("Enter a number: "))
fact = 1
i = 1

while i <= num:
    fact *= i
    i += 1

print("Factorial =", fact)



#password is correct or not

 
password = "admin123"

while True:
    user = input("Enter password: ")

    if user == password:
        print("Access Granted")
        break
    else:
        print("Wrong Password")