import sys 
print(sys.version) #this is for knowing the verrsion of python we are using
 

if 5>= 3:
    print("five is greater than three") # this is for if statement 


print("hello gyes"); print("welcome to my universe"); print("why ? you come here ? ") # this for multiple statement in one line


print(4 + 6) # this for addittion 
print(5 - 7) # this for substraction
print(3 * 4) # this for multiplication 
print(10 / 3) # this is for division 
print(5%2) # this is for modulas 


print("i am",17,"year old") #You can combine text and numbers in one output by separating them with a comma


x = 5
y = "harit"
print(x) # this is the way to print the value of x 
print(y) # this is the way to print the value of y


x = 4 # x is of type int 
x = "harit" # x is now of type str
print(x) # this will print the value of x which is "harit" because we have reassigned the value of x to "harit"


x = str(3) # this will convert the integer 3 to a string "3"
y = int(3) # this will convert the string "3" to an integer 3
z = float(3) # this will convert the integer 3 to a float 3.0

print(x) # this will print the value of x which is "3"
print(y) # this will print the value of y which is 3
print(z) # this will print the value of z which is 3.0


x = 5
y = "harit"
z = 5.8765678
print(type(x)) # this will print the type of x which is <class 'int'>
print(type(y)) # this will print the type of y which is <class 'str'>
print(type(z)) # this will print the type of z which is <class 'float'>


x,y,z = "apple" , "banana" , "cherry" # this is for assigning multiplt values to multiple variables in ine Line
print (x)
print (y)
print (z) # this will print the value of x which is "apple", the value of y which is "banana" and the value of z which is "cherry"


x = y = z = "orange" # this is for assigning the same value to multiple variable in one line
print(x) # this will print the value of x which is "orange"
print(y) # this will print the value of y which is "orange"
print(z) # this will print the value of z which is "orange"


fruit = ["apple", "banana", "cherry"] # this is for creating a list of fruits
x = y = z = fruit # this is for assigning the same list to multiple variables in one line
print(x) # this will print the value of x which is ["apple", "banana", "cherry"] because we have assigned the value of x to the list fruit in the previous line
print(y)    # this will print the value of y which is ["apple", "banana", "cherry"] because we have assigned the value of y to the list fruit in the previous line
print(z) # this will print the value of z which is ["apple", "banana", "cherry"] because we have assigned the value of z to the list fruit in the previous line


x = "python"       
y = "is" 
z = "awesome" 
print(x,y,z) # this will print the value of x which is "python", the value of y which is "is" and the value of z which is "awesome" with a space in between each value because we have used a comma to separate the values in the print statement


x = "python"       
y = "is" 
z = "awesome" 
print(x + y + z ) # this will print the value of x which is "python", the value of y which is "is" and the value of z which is "awesome" without any space in between each value because we have used the + operator to concatenate the values in the print statement


x = "awesome" 

def myfunc():
    print("python is " + x) # this will print the value of x which is "awesome" because we have used the + operator to concatenate the value of x with the string "python is " in the print statement

    myfunc() # this will call the function myfunc and execute the code inside the function which will print "python is awesome" because we have assigned the value of x to "awesome" in the previous line


x = "awesome" 

def myfunc():
    x = "fantastic"
    print("python is" + x)

    myfunc()
    print("python is" + x) # this will print the value of x which is "awesome" because we have assigned the value of x to "awesome" in the previous line and then we have called the function myfunc which will print "python is fantastic" because we have assigned the value of x to "fantastic" inside the function and then we have printed the value of x again which will print "python is awesome" because we have assigned the value of x to "awesome" in the previous line and the value of x inside the function does not affect the value of x outside the function
        

x = "awesomr"

def myfunc():
    global x # this is for using the global variable x inside the function myfunc
    x = "fantastic" # this will change the value of x to "fantastic" because we have used the global keyword to indicate that we want to use the global variable x inside the function myfunc

    myfunc() # this will call the function myfunc and execute the code inside the function which will change the value of x to "fantastic" because we have used the global keyword to indicate that we want to use the global variable x inside the function myfunc and then we have printed the value of x which will print "fantastic" because we have changed the value of x to "fantastic" in the previous line
    print("python is " + x) # this will print the value of x which is "fantastic" because we have changed the value of x to "fantastic" in the previous line and then we have printed the value of x which will print "python is fantastic" because we have used the + operator to concatenate the string "python is " with the value of x which is "fantastic"


x = 1   #int
y = 2.7 #float
z = 7j  #complex

print(type(x)) # this will print the type of x which is <class 'int'> because we have assigned the value of x to 1 which is an integer
print(type(y)) # this will print the type of y which is <class 'float'> because we have assigned the value of y to 2.7 which is a float
print(type(z)) # this will print the type of z which is <class 'complex'> because we have assigned the value of z to 7j which is a complex number


x = 35e5 # this is for scientific notation which means 35 * 10^5
y = 12E4 # this is for scientific notation which means 12 * 10^4
x = -87.7e100 # this is for scientific notation which means -87.7 * 10^100

print(type(x)) # this will print the type of x which is <class 'float'> because we have assigned the value of x to 35e5 which is a float
print(type(y)) # this will print the type of y which is <class 'float'> because we have assigned the value of y to 12E4 which is a float
print(type(z)) # this will print the type of z which is <class 'float'> because we have assigned the value of z to -87.7e100 which is a float


x = 3 + 5j # this is for assigning a complex number to x which is 3 + 5j
y = 5j # this is for assigning a complex number to y which is 5j
z = -5j # this is for assigning a complex number to z which is -5j

print(type(x)) # this will print the type of x which is <class 'complex'> because we have assigned the value of x to 3 + 5j which is a complex number
print(type(y)) # this will print the type of y which is <class 'complex'> because we have assigned the value of y to 5j which is a complex number
print(type(z)) # this will print the type of z which is <class 'complex'>





x = 1 # this is for assigning the value of x to 1 which is an integer
y = 2.8 # this is for assigning the value of y to 2.8 which is a float
z = 1j # this is for assigning the value of z to 1j which is a complex number

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b)) 
print(type(c))


import random 

print(random.randrange(1,10)) # this for random number choosse


x = int(1)    # x will be 1
y = int(2.8)  # y will be 2
z = int(3)    # z will be 3

print(x)
print(y)
print(z)


x = float(1)   # x will be 1.0
y = float(2.5) # y will be 2.5
z = float(3)   # z will be 3.0
w = float(4.2) # w will be 4.2

print(x)
print(y)
print(z)
print(w)


x = str("harit")  # x will be harit
y = str(1)        # y will be 1
z = str(2.5)      # z will be 2.5

print(x)
print(y)
print(z)


a = "hello"
print(a) # this is for creating a string using double quotes

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)                              # this is for creating a multi line string using triple double quotes


a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)                              # this is for creating a multi line string using triple single quotes


a = "Hello , World !"
print(a[1])# this is for accessing the second character of the string a which is "e" because the index starts from 0
print(a[0])# this is for accessing the first character of the string a which is "H" because the index starts from 0 
print(a[2:5]) # this is for accessing the characters from index 2 to index 4 of the string a which is "llo" because the index starts from 0 and the end index is exclusive


for x in "banana":
  print(x) # this is for looping through the characters of the string "banana" and printing each character on a new line because we have used a for loop to iterate through the string and print each character



a = "Hello, World!"
print(len(a)) # this is for getting the length of the string a which is 13 because there are 13 characters in the string "Hello, World!" including the space and the punctuation\

