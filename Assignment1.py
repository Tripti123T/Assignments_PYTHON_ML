## Ques1
a = int(input("Enter one number: "))
b = int(input("Enter second number: "))
print("Sum of two number: ",a+b)


## Ques2
num = 45
if(num%2==0):
    print("Even number")
else:
    print("Odd number")


## Ques3
import math as mt
c = 5
print("Factorial is: ",mt.factorial(5))


## Ques4
str = input("Enter your name: ")
print("Hello! {}, Good Morning!".format(str))


## Ques5
str = input("Enter a string: ")
samplefile = open(r'C:/Users/tript/OneDrive/Desktop/PYTHON ML/demo.txt' ,'r')
print(str , file = samplefile)


## Ques6
with open(r'C:/Users/tript/OneDrive/Desktop/PYTHON ML/demo.txt' ,'r') as file:
    samplefile = file.read()
    print(samplefile)


## Ques7
str = input("Enter a string: ")
print("Length of this string: ",len(str))


## Ques8
str1 = "Hello "
str2 = "Tripti"
res = str1 + str2
print("After concatenation: ", res)


## Ques9
str = "Hello I am an Engineer "
substr = "I"
print(substr in str)


## Ques10
str = "Hello I am an Engineer "
str2 = str.upper()
print("Upper case string: ", str2)


## Ques11
n = int(input("Enter n number for fibonacci series: "))
a , b = 0 , 1
count =0
if(n<=0):
    print("Please enter a positive integer")
elif n==1:
    print("Fibponacci sequence up to", n , ":")
    print(a)
else:
    print("Fibonacci sequence:")
    while count< n:
        print(a, end=' ')
        nth = a+b
        a=b
        b=nth
        count +=1


## Ques12
num = 3456
sum = 0
while num > 0:
    lastdig = num % 10
    sum += lastdig
    num = num // 10

print("Sum of digit in given number: ",sum)  


## Ques 13
DOB = int(input("Enter your birth year: "))
curr = int(input("Enter current year: "))
age = curr - DOB
print("Age :", age)


## Ques 14
str = input("Enter: ")
print(str)
while str != "":
    str = input("Enter: ")
    print(str)


## Ques 15
import csv
with open(r'C:/Users/tript/OneDrive/Desktop/PYTHON ML/new_file.csv',mode ='r') as file:
    samplefile = csv.reader(file)
    for row in samplefile:
        print(row)


## Ques 16
str = "Tripti Sinha"
print("The input string is:",str)
mySet = set(str)
for element in mySet:
    countOfChar = 0
    for character in str:
        if character == element:
            countOfChar += 1
    print("Count of character '{}' is {}".format(element, countOfChar))



## Ques 17
str = "i am a strong personality"
print(str.title())


## Ques 18
str1 = "Teacher"
str2 = "Cheater"

str1 = str1.lower()
str2 = str2.lower()

if(len(str1) == len(str2)):

    s_str1 = sorted(str1)
    s_str2 = sorted(str2)

    if(s_str1 == s_str2):
        print(str1 + " and " + str2 + " are anagram")
    else:
        print(str1 + " and " + str2 +" are not anagram")
else:
    print(str1 + " and " + str2 +" are not anagram")



## Ques 19
#punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
str1 = "Hello!!!!!--------> My name is Doremon.<--------"
new_str =""
for char in str1:
    if char not in punctuations:
        new_str = new_str + char
print(new_str)


## Ques 20
num = []
n = int(input("Enter no. of elements: "))
for i in range(0,n):
    element = int(input())
    num.append(element)
sum = 0
for i in num:
    sum = sum + i
print("Total sum of numbers in list: ",sum)


## Ques 21
list1 = ["hello", "hi", "bye", "hi", "hello"]
print("Count of 'hello' in list1 is: ", list1.count("hello"))
## ---------OR------------##
element = "hello"
count = 0
for char in list1:
    if char == element:
        count = count+1
print("Count of {} is: {}".format(element,count))


## Ques 22
list1 = [23,44,33,12,56,78,67,89,98,67]
print("Minimum value: " , min(list1))
print("MAximum value: ",max(list1))


## Ques 23
y = int(input("Enter 1 for celcius and 0 for fahrenheit: "))
if y==1 :
    temp = int(input("Enter temprature: "))
    farh = ((temp*9)/5)+32
    print("Temprature in farhenheit is {}".format(farh))
elif y==0:
    temp = int(input("Enter temprature: "))
    celcius = ((temp - 32)*5)/9
    print("Temprature in celcius is {}".format(celcius))
else:
    print("Make correct input value")


## Ques 24
a = int(input("ENter a number: "))
b = int(input("Enter a number: "))
op = input("Enter any (+, -, *, /) one of these operator: ")
if op == '+':
    print("a + b: ",a+b)
elif op == '-':
    print("a - b: ",a-b)
elif op == '/':
    if a>b:
       print("a / b: ",a/b)
    else:
        print("Invalid division")
elif op == '*':
    print("a * b: ",a*b)


## Ques 25
with open(r'C:/Users/tript/OneDrive/Desktop/PYTHON ML/demo.txt','r') as file:
    content = file.read()
    with open(r'C:/Users/tript/OneDrive/Desktop/PYTHON ML/text_file.txt','w') as file2:
        file2.write(content)
print("File copied!!")


## Ques 26
str = input("Enter a string: ")
suffix = "Thanks"
prefix = "Hi!"
if str.startswith(prefix):
    print("The string starts with '{}'.".format(prefix))
else:
    print("The string does not start with '{}'.".format(prefix))

if str.endswith(suffix):
    print("The string ends with '{}'.".format(suffix))
else:
    print("The string does not end with '{}'.".format(suffix))


## Ques 27
str = "Hello all! Welcome to this lecture"
print("List of string: ",list(str))
