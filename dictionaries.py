# DAY - 3
# read up on dictionaries
# dictionatry = {}
# dictonary[key] = value 
# print(dictionary.keys())
# print(dictionary.values())
""" Find avg """
print(f"\n1.Find avg")
grades = {'Alice': 85, 'Bob': 90, 'Charlie': 78, 'David': 92}
size = len(grades)
total = sum(grades.values())
items = grades.items()
print(f"for grades = {grades}\naverage = {total/size}")

""" use dict.items """
for key,items in grades.items():
    print(f"{key}: {items}")


# if 'Meenu' not in grades.keys():
#     grades['Meenu'] = 0

# print(grades['Meenu'])
# print(grades['Meenu.a'])
""" get """
print(f"\n1.a. using get function grades.get('Meenu',0) = {grades.get('Meenu',0)}")

""" Collections """
#default dict - faster
# Count he frequency of each word in a list of words

""" count fruits """
print(f"\n2.count fruits")
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
mycount = {}
# sample output {'apple': 3, 'banana': 2, 'orange': 1}
for item in words:
    if item not in mycount:
        mycount[item] = 1
    else:
        mycount[item] += 1
print(f"count = {mycount}")

"""
Student Grade Management
Scenario: You are developing a student grade management system for a school. 
Each student has a unique ID and a list of courses they are enrolled in, along with their grades in each course. 
You need to calculate the GPA for each student and identify the student with the highest GPA.

Question: Write a function that takes a dictionary representing the students (student IDs as keys and a dictionary of 
courses and grades as values) and returns a dictionary of GPAs for each student and the student ID with the highest GPA.

"""
print(f"\n3.Student Grade Management")
# mystudent = {
#     student1:{course1:grade1,course2:grade2},
#     student2:{course1:grade1,course2:grade2}
#  }
students = {
    "S001": {"Math": 90, "Science": 85, "English": 88},
    "S002": {"Math": 78, "Science": 82, "English": 80},
    "S003": {"Math": 92, "Science": 91, "English": 89},
    "S004": {"Math": 92, "Science": 91, "English": 89}

}
gpas = {}
total_score = 0
highest_gpa = float("-inf")
for student_id,courses in students.items():
    total_score = sum(courses.values()) #["Math"],student_id["Science"],student_id["English"])
    num_of_subs = len(courses)
    gpa = total_score/num_of_subs
    gpas[student_id] = gpa
    if gpa > highest_gpa:
        highest_gpa = gpa
        highest_gpa_students = [student_id]  
    elif gpa == highest_gpa:
        highest_gpa_students.append(student_id)  
    
#     return gpas, highest_gpa_students
print(f"\n GPAs= {gpas}, \nHighest GPA = {highest_gpa_students}")
# print(gpas)
# max_key = max(gpas, key=gpas.get)
# print(max(gpas, key=gpas.get))
# print(gpas[max_key])


""" HW - if multiple students get same max score, how do you print winner """
"""
 Product Review System
Scenario: You are developing a product review system for an e-commerce platform. 
Each product has a unique ID and a list of reviews. You need to add new reviews to the products and 
calculate the average rating for each product.

Question: Write a function that takes a dictionary representing the products (product IDs as 
keys and a list of reviews as values, where each review is a dictionary with user and rating), 
a product ID, and a new review. Update the product's reviews and return the updated average rating for the product.

# Example usage:
products = {
    "P001": [{"user": "User1", "rating": 4}, {"user": "User2", "rating": 5}],
    "P002": [{"user": "User3", "rating": 3}]
}
new_review = {"user": "User4", "rating": 4}

average_rating = add_review(products, "P001", new_review)
print(products)
# Output: {'P001': [{'user': 'User1', 'rating': 4}, {'user': 'User2', 'rating': 5}, {'user': 'User4', 'rating': 4}], 'P002': [{'user': 'User3', 'rating': 3}]}
print(average_rating)
# Output: 4.33

"""
print(f"\n4. Product Review System")
products = {
    "P001": [{"user": "User1", "rating": 4}, {"user": "User2", "rating": 5}],
    "P002": [{"user": "User3", "rating": 3}]
}
new_review = {"user": "User4", "rating": 4}
def add_review(products, product,new_review):
    products[product].append(new_review)
    for pr,user_ratings in products.items():
        if pr == product: 
            print(f"\nproduct = {product},\nuser_ratings= {user_ratings}")
            avg = 0
            for ratings in user_ratings:
                avg += ratings['rating']
            print(f"average rating of {product}= {avg/len(user_ratings)}")


add_review(products, "P002",new_review)