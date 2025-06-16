import json
from database import ProductDB
from models import Product

# This part of the code extracts product data from a JSON file and inserts it into a dataclass model
data = []

with open('products_200.json', 'r') as file:
    data = json.load(file)

items = [Product.init(item) for item in data]



# This part of the code initializes the database and inserts the products into it

db = ProductDB(db_path="products.db")

for item in items:
    db.insert_product(item)



# This part of the code retrieves all products from the database and prints them

products = db.get_all_products()

for product in products:
    print(product)
