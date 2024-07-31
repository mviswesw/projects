"""
A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression.

Syntax
lambda arguments : expression
-----------------------------------
The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.

Syntax
map(function, iterables)
---------------------------------
"""
# write a lambda funcion to add two numbers
added = lambda a,b : a+b
print(added(1,2))
subtraceted = lambda a,b : a-b
print(subtraceted(1,2))
divided = lambda a,b : a/b
print(divided(1,2))
multiplied = lambda a,b :a*b
print(multiplied(1,2))

""" b shoudl default to 10 if not provided """
added = lambda a,b=10 : a+b
print(added(1))

""" a shoudl default to -10 if not provided """
subtraceted = lambda b,a=-10 : a-b
print(subtraceted(2))

""" create a dictionary and perfrom all operations """
print("create a dictionary and perfrom all operations")
operations = {
              "added": lambda a,b:a+b,
              "subtraceted" : lambda a,b : a-b,
              "divided" : lambda a,b : a/b,
              "multiplied" : lambda a,b :a*b
              } 
print(f'added {operations["added"](1,2)}') # note the single quote
print(f'subtraceted {operations["subtraceted"](1,2)}') # note the single quote
print(f'divided {operations["divided"](1,2)}') # note the single quote
print(f'multiplied {operations["multiplied"](1,2)}') # note the single quote

""" squares and cubic powers """
print("\nsquares and cubic powers")
# note the paranthesis
print(f"{(lambda a: a*a)(5)}")


print("\nsquares")
a = [1,3,5,6,3,6]
# for i in a:
#     print("sqare", i*i)
#     print("cube",i*i*i)

def square(s_value):
    return s_value*s_value

def cube(value):
    return value*value*value

for i in a:
    print(i)
    print(square(i))
    print(cube(i))
    print("*****")

""" MAP
TLDR - map perform for loop for a function
"""
numbers = [1,3,5,6,3,6]
# map(func,iteration)

# lambda a: a*a
var = list(map(square,numbers))
print(var)

""" Lambda + MAP """
var = list(map(lambda x:x*x,numbers))
print(var)

# def square(x):
#     return x * x
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = list(map(square, numbers))
# print(squared_numbers)

""" HW - play with lambda and map  - 10 example """
""" example 1 """
