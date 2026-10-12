
#37 - WORKING WITH SPREADSHEET WITH PYTHON

import openpyxl as xl
from openpyxl.chart import BarChart, Reference

#automatine the process of updatind the workbook
# you pass the file name yu want to automate get the file in a directory and the code would uodate your spreadsheet

def process_workbook(filename):
    wb = xl.load_workbook('filename')
    sheet = wb['Sheet1']
    cell =sheet['AI']
    cell = sheet.cell(1,1)
    print (cell.value) # to see the cell value from your workbook
    print(sheet.max_row) # to see the number of roes in your workbook

    for row in range(2, sheet.max_row + 1): # oni is because the range function will generate the first three not he last on as would a range function so we add on ro add one more
        #we wnt to ignore te first row
        cell = sheet.cell(row,3)
        corrected_prices = cell.value * 0.9
        corrected_price_cell = sheet.cell(row,4 )
        corrected_price_cell.value = corrected_prices

    values = Reference(sheet, min_row =2, max_row =sheet.max_row,
              min_col = 4, max_col =4)
    #to select a range of values, the constructor,
    chart = BarChart()
    chart.add_data(values)
    sheet.add_chart(chart,'e2')

#wb.save('transactions2.xlsx') #to save your workbook
#use tis files to save your workbooks

#to access the cell in an excel workbook, we use either of the two, labelling of cells is case sensitive, use square bracket combination of the row and column A3 use the cell method of the sheeet object pass tge row and the column,
#how many rows we have in the spreedhseet. sjeet has an atyribute caled max


def greetuser():
    print('Hi there')
    print('Welcome aboard ')

print('Start')
print(greetuser())
print('Finish')

import math

print(math.floor(2.8))

# first exercise - PRINT FUNCTION: to print out your name, a dog and a smiley face on the terminal.
print('Hello Rachael')
print('o----')
print(' ||||' )
print(''' This is a dog''')
print('^' * 3)
print('o o')
print(' -')
print(''' This is a smily face''')

# second exercise - DATA TYPES: learnt about integers, float, boolean and strings
price = 10
print(price)

# third exercise - PRINT & VARIABLES: more printing exercise on the terminal
experiment = 'John Smith'
age2 = '20'
existing_or_new = 'New'

# fourth exercise - INPUT FUNCTION: the use of an inbuilt function input used to recieve input from the user. And also learnt how to concatonate
name = input(' What is your name? ')
bool(name)
print(name)
fav_colour = input('What is your favourite colour? ')
print(name + ' likes ' + fav_colour)

# fifth exercise - DATA TYPE: to find the type of the variable or text or number,
# you use the type function to find the variable type and also learning how to convert your code to the expected output
# you'd see or when calculating for it to align and work out smoothly
birth_year = input('Birth year :')
age = 2026 - int(birth_year)
print(type(age))
# the output printed out is the type how do i also print out the age calculated as well? print it without the type
# Why do we use quotations using the input function, why can't it just be bare?

# sixth exercise - CONVERTING DATA TYPES : a simple code to convert your weight from kg to pounds.
# also to not forget to change the returned value(which in this case it is a string) to the desired output(an integer)
weight = input('How much do you weigh in kg? ')
converted = int(weight) / 0.45
print(converted)

# eight exercise - FORMATTED STRINGS: they are placeholders (holes) in your code or input a variable you want to add.
# It creates holes in your strings, it makes it easier to visuaize the outputs and what it looks like, prefixed with an f. it uses curly braces.
first = 'John'
last = 'Smith'
msg = f'{first} {last} is a coder'
print(msg)

# seventh exercise/ ninth exercise :  a course variable, you can use both single and double quotes to define a variable,
# but you have to be careful when using it, multiple line we use triple quotes, use square brackets at a given index an indexing starts at 0,
# to call it, you get character you want to get. -1 to get the character from the back.
# if you want to select a range, you use the range of 0: 4 to the character index you want it to stop.
# if you want the full code, it will just be a square with (a colon):bracket.
course = 'Python for beginners'
print(len(course))
course.find('G')
# len function to also print he lenght of the results. theses are string methods, to access these functions you use the operators,
# (course. upper) some are general purpose function, some are particular to stings of a function created. .lower, .upper,
# .find(to find the sequence of characters in a string the index of the first occurance of that character,
# the find method is case-sensitive so if you pass O when it is o is will come out as  -1 because is not on the string/text ),
# replace to replace what you want (previous, new) and it is case sensitive, you can also replace a single character.
# to check the existence of a character if the string contains the word you are looking for you user the in function
# (a boolesn exoression it will return a boolean value(true or false )
# vwhat  the couput will give is a duplicate of course, does that mean that : can work as a duplicate?

# tenth exercise - ARITHMETIC OPERATORS & OPERATION: division with / will return a float, with a // will return an integer,
# modulos(%) returns the remainder of the division, the exponent that is 3 raise to power 4 ,
# an augmented assigned operator x += 3 enhance the operator that is 3 plus x equals the new value= =+ 
# the same code but in a shorter form (order of operation - BODMAS) exponentiation, multiplication/division, addition/subtraction,
# use parantesis to change the order of preferences, it always takes priority,
# math functions, working with numbers, round function, to round it up to the nearest number, 
# absolute function always returns the positive function of hr value (abs) import the math module with reusesble code to work with mat functions, 
# ceil function to get the ceiling of a number, floor method the get the floor of a number.
x =10
x = x + 3
print(x)

x = 10
x+=4
print(x)

# 11th exercise - CONDITIONAL STATEMENTS: make decisions based on some conditions,
# If this is this do this if not do this (if, else, elif)  absence of heat does not mean it is cold.
# It is also used to build rules as well.

is_hot = False
is_cold = False
if is_hot:
    print('It is a hot day')
    print('Drink plenty of water')
elif is_cold:
    print('It is a cold day')
else:
    print('Take an umbrella with you')
    print('Wear warm clothes')

print('Enjoy your day')

house_price = 1000000
good_credit = False

if good_credit:
    price = 0.1  * int(house_price)
    print(f'You need to put down ${price} ')
else:
    price = 0.2 * int(house_price)
    print(f'You need to put down ${price}')

#12th exercise - LOGICAL OPERATORS - AND operator(if both conditions are true the program will run)
# OR if at least one of them is correct, the program will run if either of the conditions are meet it should go through.
# NOT prints the opposite 'and not X do this' it is the opposite of the answer.

has_high_income = False
has_good_credit = True
if has_high_income and not has_good_credit:
    print('Eligible for loan')
else:
    print('HELL NAH!!!')

# 13th exercise - COMPARISON OPERATORS: compare a variable with a value, if this is this do this if not do this,
# build conditional statements,  not equal to it should be 0 =! not equals to

name = input('What is your name? ')

if len(name) < 3:
    print('name must be at least 3 characters long')
elif len(name) >50:
    print('name can be a maximum of 50 characters')
else:
    print('name looks good!')

temperature = 5
if temperature > 30:
    print("It's a hot day")
elif temperature < 10:
    print('It is a cold day')
else:
    print('It is neither hot nor cold')

# 14th exercise:  WHILE LOOPS: used to execute a block of code multiple times after the while statement,
# you write a condition as long as the condition is true the code will be repeatedly executed.

x = 5
while x <=5:
    print(x)
    x = x + 1
print('Done')

# 15th exercise: FOR LOOPS used to iterate over each character in a string.  You can define lists with square brackets,

for item in range(10):
    print(item)
# price this case is a temporary variable to hold each oth the number at each iteration

prices = [10, 20, 30]
for price in prices:
    print(sum(prices))

numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num

# 16th exercise: nested loops adding one loop inside one another, example is like a list of coordinates.

for x in range(4):
    for y in range(3):
        print(f'{x}. {y}')
# in the first iteration the inner loop y is going to be zero, it is when the inner loop completes then the control goes back to line one
# the inner loop will be executed 3 times.

integers = [5,2,3,2,2]
for z in integers:
    output = ' '
    for t in range(z):
        output += 'x'
    print(output)
# range to generata a series of number from z  temporary variable

# most times the last number in a range when called are usually exclusive, that is if you call 2 to 4 it is only 2 and 3 that will show
numbers = [3,4,5,3,2,]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

#17th exercise: 2D lists in python : a rectangular array of numbers a matrix. A 2D list is a list where each item in that list is another list
# and tht list represent the items on each row. used [] to define them.
# martix [0] returns the inner list and to access the number in the inner list you wll use [0][1]

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
for row in matrix:
    for item in row:
        print(item)

# 18th exercise: LIST METHODS/FUNCTIONS: operations You can perform on alist.
# we have the append function (to add a new item), insert (takes two values, the index position and the number you want to add),
# remove to remove an item, place the item you want to remove. To remove all the items you use the clear method, and it does not take any values.
# pop function removes the last item in a list. index method to know the index of the number you wish to know,
# you can use the in operator, that is '59 in numbers inside a print function' and it returns a boolean value
# counting the occurrence of a number that is the count function,
# sort list you use the sort method it does not return any values it just sorts the values in place and then print the list.
# if you want it in descending order you call the reverse method to reverse the list,
# copy method to get the copy of your list, it is not going to affect the second list that you created, because they are two independent lists.

baby = [4,6,4,7,4,3]
unique = []
for number in baby:
    if number not in unique:
        unique.append(number)
print(unique)
#to remove duplicates

# 19th exercise TUPLES: another important structure in python, used tO store a list of numbers. You cannot modify them
# use () to define tuples they sre immutable the only 2 methods they have are count to count the number of occurrences of an item
# and index to find the index of the first occurrence of a number, only to get information not modify

# 20th exercise - UNPACKING: you can also use unpacking with list and not only tuples
coordinates = (1,2,3)

x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

x,y,z = coordinates


# 21st exercise = DICTIONARY: to store information that comes as key value pairs, each key is associated with a value.
# none is an object tht represent to abscence of an object, each key should be unique in a dictionary

customer  = {
    'Name : Ose',
    'age : 34',
    'is_verified: True'
}
# print (customer['Name'])
# or print(customer.get(name))

# or print(customer.get(name))
 # it should be the exact same sequence of numbers that is even if it is uppercase in the dictionary, do not write lowercase of the word
# a structure that allows to map a key to a value
phone = {
    'One' :' 1',
    'Two' :'2',
    'Three' : '3',
    'Four' : '4',
    'Five' : '5',
    'Six' : 6,
    'Seven' : 7,
    'Eight': 8,
    'Nine' : 9,
    'Ten': 10}
tele =input('phone_number: ')
print(tele + phone[''])

put = ''
for character in phone:
    tele.get(character, '!')
    print(put)
#it won't shout it will just return a none value, that is the get function


# 22nd - Emoji Converter:
message = input ('>')
# the split message/function goes through the string, and anywhere it finds a character,
# it uses that a boundary to seperate the multiple string, and it will return as a list.

words = message.split(' ')
emojis = {
    ':)' : '☺️',
    ':(' : '️😔'
}
end = ''
for word in words:
    end += emojis.get(word,word) + ' '
print(end)


# 23rd - FUNCTIONS: chuncks of code a container for a few lines of code that perform a specific task.
# def is the short form for define it is usd to define af function in python.
# each of the functions knows which tasks they would perform example, print. a function also comes with a bracket when defined

def greetuser():#whenever you call this function the line of code indented in it, and it will run THE CODE INDENTED IN IT
    # add two blank lines after a function, best practices for code cocumentation (PEP 8)
    print('Hi there')
    print('Welcome aboard ')


print('Start')
print(greetuser())
print('Finish')

# 24 - PARAMETERS AND POSITIONAL ARGUMENTS : pass information to your functions. Parameters are placeholders for receiving information
# print takes info but the function does not take information.

def greet_user(name):
    print(f'Hi {name}!')
    print('Welcome aboard ')

print('Start')
greet_user('John')
greet_user('Mary')
print('Finish')

# does that mean I do not need to provide my name within the backend code for my name to appear
# which part of the part of the code is the name asked for? what is the difference between parameters and formatted strings
# must you pass a value to a function when called? or a parameter? positional argument is the value tht you supply to a function
# diff between parameters (holes or placeholders used to define in a function for receiving information is that like input)
# positional arguments are the actual piece of information that we supply to this information, adding a second parameter

def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard ')

print('Start')
greet_user('John', 'Smith') # at this point did we create a positional argument/keyword argument?
print('Finish')

# 25 - POSITIONAL ARGUMENTS AND KEYWORD ARGUMENTS
def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard ')

print('Start')
greet_user('John', 'Smith') # referred to as positional that is their position matters,
# key word arguments the postion doesn't matter, parameter name followed by its value
greet_user(first_name ='John', last_name='Smith') # key word argument should always come after positional argument if mixing PA first KWA next
print('Finish')

#26 RETURN FUNCTION: to return the result, example of a calculation function.
def square(number):
    return number * number

square(3) #or
result = square(3)#or
print(square(3))

# do you only use return in a function? if return not used, all functions in python return none
# if you want it to return something with the return function

# assignment: extract a function from this code
message = input ('>') # input can come in a different Graphic User interface because the line won't be reusable replace it with a string.
words = message.split(' ')
print(end)
# not the last line what we do with the output would be different it should not belong to a function recieving information and sending out information
def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ':)' : '☺️',
        ':(' : '️😔'
    }
    end = ''
    for word in words:
        end += emojis.get(word,word) + ' '
    return end

message = input('>')
print(emoji_converter(message))

# 27th - EXCEPTIONS: how to handle error in python: exit code 0 code succeeded successfully, value error it is more of a datatype program,
# exit code 1 or any other  number meant that your code crashes.
#an exception is a kind of error that crashes our program, value type error non-numerical value to an integer for the value, zero division error

try:
    age = int(input('Age: '))
    print(age)
except ValueError:
    print('Invalid value')

# 28th - COMMENTS: used comment to add notes to your program, bad comment, explaining what the code does,
# the obvious sentence of what the code is going to print exactly, whys and hows that is when you use comments, remainders or making assumptions


# 29th - CLASSES: classes uses it to define new types, integers, boolean,strings, complex types are lists and dictionaries.
# We cannot always model complex concept. It is used to create somewhat complex concepts, variables and functions should be in lowercase and underscore
# no underscore for classes only capitalize the first letter of every word new pascal naming convention.

# define all the functions and methods you want to add to the class method
# difference between creating functions and methods under the class function?
# use the newly created type to create new object, an object is an instance of a class.
# class simply defines the blueprint or the template for creating objects. objects are instance based on the blueprints
#attributes are variables that belongs to a particular object
#we use classes to define new types with methods and attributes we can set anywhere in the code
# evey method in a class should have self parameter, and it should be the first of the class method defined in the class

class Point: # os point in this case an object or a defines type or an object
    def  move(self): #self is  a special keyword
        print('move')
    def draw(self):
        print('draw')


point1 = Point
point1.x = 10 #attributes
point1.y = 20 #attributes
print(point1.x)
point1.draw()


# 30th - CONSTRUCTOR: a constructor is a function that gets called when creating an object.
# init is  short for initialized, used when we call anew object
#self is a reference to the current object, why can't we create an object without the init function
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def  move(self):
        print('move')
    def draw(self):
        print('draw')


point = Point(10, 20)
print(point.x)

class Person:
    def __init__(self, figure): #a constructor, figure is also equals to name
        self.figure = figure

    def talk(self):
        print('talk')


john = Person()
print(john.figure)
john.talk()


#31 - INHERITANCE: a mechanism for reusing code. #other mechanisms for reusing code?
class Dog:
    def walk(self):
        print('walk')

#define a new class mammmal and define the similar classes to it
# if you want to create a cat and dog function, it is possible if it is going to be similar,
# so you define as particular class like mammal then move the piece of code to it then you can use it any [art of your code
class Mammal:
    def walk(self):
        print('walk')

class Dog(Mammal):
    pass # python doesn't like an empty string so it would use a pass function to pass it


class Cat(Mammal):
    def be_annoying(self):
        print('annoying')


cat1 = Cat()
cat1.be_annoying()


#32 - MODULES: modules with python, files with python code used to organize our code into multiple files,
#converters a module should create all the related functions and classes
import converters
#can you use the import function in any part of the code, must it be the top?

import converters
from converters import kg_to_lbs

kg_to_lbs(100)

from utiles import find_max

#purple used to identify builtin functions, created a utiles module to find the maximum of a number in a list

#33 - PACKAGES: Packages are used to organize your codes, a container for multiple modules, a package is a directory or folder.

import ecommerce.shipping
ecommerce.shipping,calc_shipping()

from ecommerce.shipping import calc_shipping #to from a modules then a class then a function that you would call at that particular time
from ecommerce import shipping  # from a module import a function that you would call anywhere in your code
#access all the functions and classes with the dot operator

#34 - GENERATING RANDOM VALUES: modules are already built into python (python 3 module index) you can see all the modules built into python
import random
for i in range(3):
    print(random.random())
    print(random.randint(10, 20))

#randomly pickes a member from the lists and prints it out
members = ['John', 'Mary', 'Bob', 'Mosh']
leader = random.choice(members)
print(leader)

import random
class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second #when you want to return a tuple you use a parentheses,
        # or you can remove them, python code interprets as a tuple e.g return 2, b

dice = Dice()
print(dice.roll())

#35 - FILES AND DIRECTORIES
from pathlib import Path

#absolute or relative: relative is from the current directly, absolute takes code directly from our local disk
path = Path('ecommerce')
print(path.exists()) # to check if a path exists

path = Path('emails')
print(path.mkdir()) # to create a directory, rmdir is used to remove directly,
# to search for files and directories in the current path use the star symbol (*)

path = Path()
print(path.glob('*')) # asterisk to see all the files star . star or star.py or xls (generated objects)?

#36 - PYPI & PIP: python packages Index, pypi.org packages you can use built by developers you would not need to create some functions again
# yelp? web scrapping? mean used the engine to browse a website to extract info from html files browser automation testing of your web applications

# how do i see all the files/packages I have installed? go the python files and click on site you will see it, access if from your project panel
# pathlib: object oriented file system paths used to provide classes we can use to create objects to work with directories and fies
# from pathlib import
#absolute or relative, path() if you do not input a file inside it, it would show the current directory
# search for files and directory in that path?
path = Path()
for file in path.glob('*.py'):  #because of the object generator we iterate over the path, that is the for loop
    print(file)

# PyPi openpyxl used your work with spreadsheet pip used to install packages on pypi.org to also uninstall use pip

#37 - WORKING WITH SPREADSHEET WITH PYTHON

import openpyxl as xl

wb = xl.load_workbook('transactions.xlsx')
sheet = wb['Sheet 1']
cell =sheet['AI']
sheet.cell(1,1)
print ('cell.value')


lecture = ''' 28TH JANUARY 2025 = REVISION CLASS ON PREVIOUS 1 HR VIDEO ON PYTHON
An integer is a number without a decimal point. Use an underscore to separate multiple variables as well as to 
define variable make sure it begins with a variable. A piece of code that produces an expression. 
Index on python code, starts at O but if you use a bracket to define 0 to 3 it will print everything except the 3rd index 
In the case of the another, you can print out the same expression in the same as in like photocopy in a different part of the app layout, 
all you have to do is define 'another' variable with the expected variable inside plus the : this quote and print it out formatted srings, 
creating holes in the expression and filling them with the assigned variable. Use len functions to find the lenght  in a string, 
you can use the in operator to check if its in a string. Absolute always returns a positive values'''
