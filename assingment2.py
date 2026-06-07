#assingment2

#function in python

#check positive,negative or zero

def check(n):
    if n>0:
        print("Positive number")
    elif n<0:
        print("Negative number")
    else:
        print("Zero")


n=int(input("Enter number:"))
check(n)   


#even odd number

def even_odd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

num = int(input("Enter a number: "))
even_odd(num)


# Greater of Two Numbers

def greater(a, b):
    if a > b:
        return a
    else:
        return b

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("Greater number =", greater(x, y))


# Greater of Two Numbers

def vote(age):
    if age >= 18:
        print("Eligible to vote")
    else:
        print("Not eligible to vote")

age = int(input("Enter age: "))
vote(age)


#Divisible by 5

def divisible_by_5(n):
    if n % 5 == 0:
        print("Divisible by 5")
    else:
        print("Not divisible by 5")

num = int(input("Enter a number: "))
divisible_by_5(num)


#Leap Year

def leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")

year = int(input("Enter year: "))
leap_year(year)



#Vowel or Consonant

def check_char(ch):
    if ch.lower() in "aeiou":
        print("Vowel")
    else:
        print("Consonant")

c = input("Enter a character: ")
check_char(c)



#Largest Among Three Numbers


def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    else:
        return c

x = int(input())
y = int(input())
z = int(input())

print("Largest =", largest(x, y, z))


#Sum from 1 to 100

def sum_100():
    s = 0
    for i in range(1, 101):
        s += i
    print("Sum =", s)

sum_100()



#Multiplication Table

def table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

num = int(input("Enter a number: "))
table(num)


#Square of a Number

def square(n):
    return n * n

num = int(input("Enter a number: "))
print("Square =", square(num))


#Factorial Using Loop

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

num = int(input("Enter a number: "))
print("Factorial =", factorial(num))


#Check Prime Number

def prime(n):
    if n <= 1:
        print("Not Prime")
        return

    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            return

    print("Prime")

num = int(input("Enter a number: "))
prime(num)


#Sum of Digits

def sum_digits(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

num = int(input("Enter a number: "))
print("Sum of digits =", sum_digits(num))



#Sum from 1 to n

def sum_n(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s

num = int(input("Enter n: "))
print("Sum =", sum_n(num))


#list in python

#Create a list of 10 numbers and print all elements

lst = [1,2,3,4,5,6,7,8,9,10]

for i in lst:
    print(i)
    
    

#Find the largest element in a list

lst = [10, 25, 8, 45, 12]

largest = max(lst)

print("Largest element =", largest)



#Find the smallest element in a list

lst = [10, 25, 8, 45, 12]

smallest = min(lst)

print("Smallest element =", smallest)


#Calculate the sum of all elements in a list

lst = [10, 20, 30, 40, 50]

total = sum(lst)

print("Sum =", total)


#Calculate the average of all elements in a list

lst = [10, 20, 30, 40, 50]

average = sum(lst) / len(lst)

print("Average =", average)


#Count how many even numbers are present in a list

lst = [1, 2, 3, 4, 5, 6, 8]

count = 0

for i in lst:
    if i % 2 == 0:
        count += 1

print("Even numbers =", count)


#Create a new list containing only odd numbers

lst = [1, 2, 3, 4, 5, 6, 7, 8]

odd_list = []

for i in lst:
    if i % 2 != 0:
        odd_list.append(i)

print("Odd numbers list =", odd_list)



#Check whether an element exists in a list

lst = [10, 20, 30, 40, 50]

num = int(input("Enter element: "))

if num in lst:
    print("Element found")
else:
    print("Element not found")
    
    
    
#Reverse a list without using built-in reverse functions

lst = [1, 2, 3, 4, 5]

rev = []

for i in lst:
    rev = [i] + rev

print("Reversed List =", rev)



#Find the second largest element in a list

lst = [10, 25, 8, 45, 30]

lst.sort()

print("Second Largest =", lst[-2])



#Python Dictionaries 

#Create a dictionary and print it 

student = {
    "name": "Rahul",
    "age": 20,
    "city": "Mumbai"
}

print(student)


#Print all keys of a dictionary

student = {
    "name": "Rahul",
    "age": 20,
    "city": "Mumbai"
}

for key in student.keys():
    print(key) 


#Print all values of a dictionary

student = {
    "name": "Rahul",
    "age": 20,
    "city": "Mumbai"
}

for value in student.values():
    print(value)
    

#Add a new key-value pair

student = {
    "name": "Rahul",
    "age": 20
}

student["city"] = "Mumbai"

print(student)


#Check whether a key exists

student = {
    "name": "Rahul",
    "age": 20,
    "city": "Mumbai"
}

key = input("Enter key: ")

if key in student:
    print("Key exists")
else:
    print("Key does not exist")
    
    
#Remove a key-value pair

student = {
    "name": "Rahul",
    "age": 20,
    "city": "Mumbai"
}

del student["city"]

print(student)


#Count total number of key-value pairs

student = {
    "name": "Rahul",
    "age": 20,
    "city": "Mumbai"
}

print("Total pairs =", len(student))



#Print all keys and values

student = {
    "name": "Rahul",
    "age": 20,
    "city": "Mumbai"
}

for key, value in student.items():
    print(key, ":", value)
    
    


#Find the student with highest marks

marks = {
    "Rahul": 85,
    "Amit": 92,
    "Priya": 88,
    "Neha": 95
}

highest = max(marks, key=marks.get)

print("Topper =", highest)
print("Marks =", marks[highest])