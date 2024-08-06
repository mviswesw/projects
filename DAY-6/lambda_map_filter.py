# fruits = ['apple', 'banana', 'cherry']
# print(fruits[0].upper())


# for i in fruits:
#     print(i.upper())

# """ 1. convert list to uppercase """
# print("\n1. convert list to uppercase")
# print(list(map(lambda i: i.upper(), fruits)))

# """ 2. convert to lowercase """
# print("\n2. convert to lowercase")
# print(list(map(lambda i:i.lower(),fruits)))

# """ 3. print first word of each item on the list """
# print(" \n3. print first word of each item on the list")
# desserts = ['apple pie', 'banana split', 'cherry tart']
# for i in desserts:
#     print(i.split())
# print(list(map(lambda i:i.split()[0],desserts)))

# """ print last word (2nd word) """
# print("\n print last word (2nd word)")
# print(list(map(lambda i:i.split()[-1],desserts)))

# """ 2nd letter of 1st element """
# print("\n 2nd letter of 1st element")
# print(list(map(lambda i:i.split()[0][1],desserts)))


"""" Filter """
# function that filters vowels
print("\nfunction that filters vowels")
def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False


# sequence
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

# using filter function
filtered = filter(fun, sequence)

print('The filtered letters are:')
for s in filtered:
    print(s)

""" print odd and even numbers by doing filter from a list """
print("print odd and even numbers by doing filter from a list")
numbers = [1,2,3,-3,-4,5,6,7,8,9,10,11,12,1,3,14,15]
print(f"\nEVEN = {list(filter(lambda num:num%2==0 ,numbers))}")
print(f"\nODD = {list(filter(lambda num:num%2>0 ,numbers))}")

""" write sentance - if 2nd letter of each word is vowel, print it """
print("\nwrite sentance - if 2nd letter of each word is vowel, print it")
sentance = "Meenu is Awesome! She is a also great person"

def is_vowel(word):
    # print(word)
    # print(len(word))
    if len(word)>2:
        if word[1] in ['a','e','i','o','u']:
            return True

# list(map(lambda word: word[1] in ['a','e','i','o','u']),sentance.split()),
result = list(map(lambda word: len(word) > 2 and word[1] in ['a', 'e', 'i', 'o', 'u'], sentance.split()))
mylist = list(filter(is_vowel,sentance.split()))
print(result)

""" HW - get a list of example simple problems - map and filer combined """

