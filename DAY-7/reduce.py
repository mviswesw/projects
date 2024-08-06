"""
reduce
"""
import functools

# initializing list
lis = [1,2]

# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a,b: a*b, lis))

# # using reduce to compute maximum element from list
# print("The maximum element of the list is : ", end="")
# print(functools.reduce(lambda a, b: a if a > b else b, lis))

inpWords = ['here','is','a','list','of','words']
print(functools.reduce(lambda a,b:a+" "+b,inpWords)) 

numbers = [1,2,3,4,5] # 6,7,8,9,10
print(functools.reduce(lambda a,b:a*b,numbers))

""" 
list comprehension
"""

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

print(newlist)

mynewlist = [x+"iii" for x in fruits if "e" in x]
print(mynewlist)

myfruit = [fruit for fruit in fruits if fruit=='apple']
print(myfruit)

