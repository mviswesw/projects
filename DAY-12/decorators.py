# def shout(text): 
#     return text.upper() 

# print(shout('Hello')) 
# print(shout)
# yell = shout 
# print(yell)

# # print(yell('Hello')) 

# def shout(text): 
#     return text.upper() 

# def whisper(text): 
#     return text.lower() 

# def greet(func): 
#     # storing the function in a variable 
#     greeting = func("""Hi, I am created by a function passed as an argument.""") 
#     print (greeting) 

# greet(shout) # passing a function to another function as argument
# greet(whisper) 

# def wecome(func, newtext):
#     return func(f"this is inside welcome, {newtext}")

# def hifunc(text):
#     return f"{text} hi, hello!"

# print(wecome(hifunc,"newtext"))

# def greet():
#     return "Hello, World!"

# # def call_function(func):
# #     return func()

# # result = call_function(greet)
# # print(result)  # Output: Hello, World!

# def add_one(x):
#     return x + 1
# def sub_one(x):
#     return x - 1


# def call_function(func, number):
#     return func(number)

# result = call_function(add_one, 5)
# result2 = call_function(sub_one, 5)

# print(result)  # Output: 6
# print(result2)  # Output: 6
""" -------------------------------------------- """

# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         # func()
#         print("Something is happening after the function is called.")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()
""" -------------------------------------------- """
def decorator_one(func):

    def wrapper():
        print("Decorator One: Before the function call.")
        func()

        print("Decorator One: After the function call.")
    return wrapper

def decorator_two(func):
    def wrapper():
        print("Decorator Two: Before the function call.")
        func()
        print("Decorator Two: After the function call.")
    return wrapper

@decorator_one
@decorator_two
def say_hello():
    print("Hello!")

say_hello()
""" -------------------------------------------- """
# *args, **kwargs
def show_info(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_info("Item1", "Item2", name="Alice", age=30)