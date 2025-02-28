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








