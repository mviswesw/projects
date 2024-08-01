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


"""
1. Processing Valid Emails
Question: Given a list of email addresses, use the filter() function to keep only those that contain the domain @example.com. 
Then, use the map() function to create a new list where each email is converted to lowercase.

Example Input: ['John.Doe@Example.com', 'Jane.Smith@example.com', 'Alice.Jones@otherdomain.com']
Expected Output: ['john.doe@example.com', 'jane.smith@example.com']
"""
print("***************\n")

emails = ['John.Doe@Example.com', 'Jane.Smith@example.com', 'Alice.Jones@otherdomain.com']
print(f"Input = {emails}")
# approach 1
def is_example_dot_com_lower(email):
    return ("example.com" in email.split("@")[1].lower())

result = list(filter(is_example_dot_com_lower,emails))
print(f"\nApproach 1=\nelements with example.com domain = {result}")
print(f" converted lowercase list of emails = {list(map(lambda i:i.lower(),result))}")

# Approach 2

def is_example_dot_com(email):
    # print(email)
    domain = email.split("@")[1].lower()
    return ("example.com" in email.split("@")[1].lower())
print(f"Approach 2 = \n{list(filter(is_example_dot_com,list(map(lambda i:i.lower(),emails))))}")


"""
2. Filtering and Formatting Phone Numbers
Question: Given a list of phone numbers (as strings), use the filter() function to keep only those that are valid (i.e., exactly 10 digits long). Then, use the map() function to format each phone number by adding dashes in the format XXX-XXX-XXXX.

Example Input: ['1234567890', '0987654321', '12345', '123456789012']
Expected Output: ['123-456-7890', '098-765-4321']

"""