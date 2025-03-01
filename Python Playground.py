print("Python Syntax")
print("Five is greater than two!")
print("Comment")
#This is a comment
print("Hello World")
print("Hello World!") #This is a comment.
#print("Hello World")
print("Cheers, Mate!")
x = 5
y = "John"
print(x)
print(y)
x = 4    #x is of type int
x = "Sally"   #x is now of type str
print(x)
x = str(3)
y = int(3)
z = float(3)
print(x)
print(y)
print(z)
x = 6
y = "John"
print(type(x))
print(type(y))
x  = "John"
print(x)
#Double quotes is the same as single quotes
x = 'John'
print(x)
a = 4
A = "Sally"
print(a)
print(A)
#A will not overwrite a.
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
x = y = z = "Orange"
print(x)
print(y)
print(x)
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
#The Python print() function is often used to output variables.
#Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome".
x = "Python is awesome"
print(x)
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
#For numbers, the + character works as a mathematical operator:
x = 5
y = 10
print(x + y)
#The best way to output multiple variables in the print() function is to separate them with commas, which even support different data types:
x = 5
y = "John"
print(x, y)
#Global variables can be used by everyone, both inside of functions and outside.
x = "awesome"
print("Python is " + x)
x = "awesome"
def myfunc():
    x = "fantastic"
    print("Python is  " +x)
myfunc()
print("Python is  " +x)

def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is  " +x)
print("Python is  " +y)

#ype function
x = 5
print(type (x))

#Setting the data type
x = "It's Friday"
#display x
print(x)

#display the data type of x
print(type(x))

x = 20
#display x
print(x)

#display the data type of x
print(type(x))

x = 20.5
#display x
print(x)

#display the data type of x
print(type(x))

x = 1j
#display x
print(x)

#display the data type of x
print(type(x))

x = ["apple", "banana", "cherry"]
#display x
print(x)

#display the data type of x
print(type(x))

x = ("apple", "banana", "cherry")
#display x
print(x)

#display the data type of x
print(type(x))

x = range(6)
#display x
print(x)

#display the data type of x
print(type(x))

x = {"name" : "John", "age" : 36}
#display x
print(x)

#display the data type of x
print(type(x))

x = {"apple", "banana", "cherry"}
#display x
print(x)

#display the data type of x
print(type(x))

x = frozenset({"apple", "banana", "cherry"})
#display x
print(x)

#display the data type of x
print(type(x))

x = True
#display x
print(x)

#display the data of x
print(type(x))

x = b"Hello"
#display x
print(x)

#display the data type of x
print(type(x))

x = bytearray(5)
#display x
print(x)

#display the data type of x
print(type(x))

x = memoryview(bytes(5))
#display x
print(x)

#display the data type of x
print(type(x))

x = None
#display x
print(x)

#display the data type of x
print(type(x))

#Setting the specific data type
x = str("Hello World")
#display x
print(x)

#display the data type of x
print(type(x))

x = int(20)
#display x
print(x)

#display the data type of x
print(type(x))

x = float(20.5)
#display x
print(x)

#display the data type of x
print(type(x))

x = complex(1j)
#display x
print(x)

#display the data type of x
print(type(x))

x = list(("apple", "banana", "cherry"))
#display x
print(x)

#display the data type of x
print(type(x))

x = range(6)
#display x
print(x)

#display the data type of x
print(type(x))

x = dict(name="John", age=36)
#display x
print(x)

#display the data type of x
print(type(x))

x = set(("apple", "banana", "cherry"))
#display x
print(x)

#display the data type of x
print(type(x))

x = frozenset(("apple", "banana", "cherry"))
#display x
print(x)

#display the data type of x
print(type(x))

x = bool(5)
#display x
print(x)

#display the data type of x
print(type(x))

x = bytes(5)
#display x
print(x)

#display the data type of x
print(type(x))

x = bytearray(5)
#display x
print(x)

#display the data type of x
print(type(x))

x = memoryview(bytes(5))
#display x
print(x)

#display the data type of x
print(type(x))

#Python Numbers
x = 1
y = 2.8
z = 1j

print(type(x))
print(type(y))
print(type(z))

#Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
x = 1
y = 456345675
z = -453467

print(type(x))
print(type(y))
print(type(z))

#Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
x = 1.10
y = 1.0
z = -34.56

print(type(x))
print(type(y))
print(type(z))

#Float can also be scientific numbers with an "e" to indicate the power of 10.
x = 34e6
y = 12E4
z = -87.6e100

print(type(x))
print(type(y))
print(type(z))

#Complex numbers are written with a "j" as the imaginary part
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

#You can convert from one type to another with the int(), float(), and complex() methods:
##convert from int to float
x = float(1)

#convert from float to int
y = int(2.5)

#convert from int to complex
z = complex(1)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))

#Python has a built-in module called random that can be used to make random numbers
import random
print(random.randrange(1, 10))

#Specifying variables
#Integers
x = int(1)
y = int(2.8)
z = int("3")

print(x)
print(y)
print(z)

#Floats
x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")

print(x)
print(y)
print(z)
print(w)

#Strings
x = str("s1")
y = str(2)
z = str(3.0)

print(x)
print(y)
print(z)

#Strings in python are surrounded by either single quotation marks, or double quotation marks.
print("Hello")
print('Hello')

#You can use quotes inside a string, as long as they don't match the quotes surrounding the string:
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#Assigning string to variables
a = "Hello"
print(a)

#Get the character at position 1 (remember that the first character has the position 0)
a = "Hello World!"
print(a[1])

#Since strings are arrays, we can loop through the characters in a string, with a for loop.
for x in "banana":
    print(x)

#To get the length of a string, use the len() function.
a = "Hello, World!"
print(len(a))

#To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "The best things in life are free"
print("free" in txt)

#Use it i"The best things in life are free"n an if statement
txt = "The best things in life are free"
if "free" in txt:
    print("Yes, 'free' is present")

#To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
#Check if "expensive" is NOT present in the following text:
txt = "The best things in life are free"
print("expensive" not in txt)

#Use it in an if statement
#print only if "expensive" is NOT present
txt = "The best things in life are free"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")



