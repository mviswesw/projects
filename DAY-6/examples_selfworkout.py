
print("-"*100)
"""
1. Processing Valid Emails
Question: Given a list of email addresses, use the filter() function to keep only those that contain the domain @example.com. 
Then, use the map() function to create a new list where each email is converted to lowercase.

Example Input: ['John.Doe@Example.com', 'Jane.Smith@example.com', 'Alice.Jones@otherdomain.com']
Expected Output: ['john.doe@example.com', 'jane.smith@example.com']
"""
print("\n1. Processing Valid Emails\n")

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

print("-"*100)
"""
2. Filtering and Formatting Phone Numbers
Question: Given a list of phone numbers (as strings), use the filter() 
function to keep only those that are valid (i.e., exactly 10 digits long). 
Then, use the map() function to format each phone number by adding dashes in the format XXX-XXX-XXXX.

Example Input: ['1234567890', '0987654321', '12345', '123456789012']
Expected Output: ['123-456-7890', '098-765-4321']

"""
print("\n2. Filtering and Formatting Phone Numbers")
phoneInput = ['1234567890', '0987654321', '12345', '123456789012']

valid_phonenumbers = list(filter(lambda number:len(number)==10,phoneInput))
print(valid_phonenumbers)
def format_number(number):
    valid_num = number[:3]+"-"+number[3:6]+"-"+number[6:]
    return valid_num
print(f" result = \n{list(map(format_number,valid_phonenumbers))}")
print("-"*100)

"""
3. Selecting and Adjusting Salaries
Question: Given a list of employee records where each record is a tuple (name, salary),
 use the filter() function to keep only those employees whose salary is greater than $50,000. 
 Then, use the map() function to create a new list where each salary is increased by 10%.

Example Input: [('Alice', 45000), ('Bob', 55000), ('Charlie', 60000)]
Expected Output: [(‘Bob', 60500), (‘Charlie', 66000)]

"""
print("\n3. Selecting and Adjusting Salaries")
salariesInput= [('Alice', 45000), ('Bob', 55000), ('Charlie', 60000)]
resultfilter = list(filter(lambda x:x[1]>50000,salariesInput))
print(list(map(lambda x:(x[0],round(x[1]+x[1]*0.1)),resultfilter)))
print("-"*100)