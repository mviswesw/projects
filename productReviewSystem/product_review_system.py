# DAY 4
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

import traceback
import logging
import datetime
import random
logger = logging.getLogger(__name__)
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG,format="[%(asctime)s - %(levelname)s] : %(message)s ")
# logging.Formatter("%(asctime)s;%(levelname)s;%(message)s")

def add_review(products, product,new_review):
    logger.info(f"Entered add_review() for {new_review['user']}")
    if "P0" not in product:
        raise Exception(f"Invalid product  - {product}")

    if(products.get(product)== None):
        products[product] = [new_review]
    else:
        products[product].append(new_review)
    logger.info(f"products = {products}")
    for pr,user_ratings in products.items():
        avg = 0
        if pr == product: 
            logger.info(f"product = {product}")
            logger.info(f"user_ratings = {user_ratings}")
            for ratings in user_ratings:
                avg += ratings['rating']
    logger.info(f"average rating of {product}= {avg/len(user_ratings)}")
    logger.info(f"Completed add_review()")

try:
    logger.info(f"started {datetime.datetime.now()}")
    
    # raise Exception("This is user defined exception")
    for i in range(100):
        # set product
        prod_id = random.randrange(10,40)
        prod = "P0"+str(prod_id)
        logger.info(f"Product = {prod}")
        
        # set user
        user_id = random.randrange(1,10)
        user = "User"+str(user_id)

        # set rating
        rating = random.randrange(1,5)

        # new review
        new_review = {"user": user, "rating": rating}
        # get review
        add_review(products, prod, new_review)
except Exception as ex:
    print(f"There was an error - {ex}")
    # traceback.print_tb(ex, limit = None, file = None)
    # print(traceback.format_exc())
    logger.info(traceback.format_exc())

logger.info(f"Ended {datetime.datetime.now()}")
