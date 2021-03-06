# groceries.py

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017; products desgnates list

# print(products)

# TODO: write some Python code here to produce the desired output

print (products [0])    # prints first product in list so '0' is the index data point in a list

print (type (products))    # tells you what "type" of data is products

print (products [0]["name"])  # this accesses the "name" component of index data point;

first_product = products [0]     # "name" component/ attribute is a dictionary data type; {} separate the different "ids"
print (type (first_product))    # tells type of data in index data point of list

print (len(products))     # function len counts number of products in list

for p in products:        # use the editor's auto populate function by typing tab and reduce syntax error
    print (p)             # prints iterative and sequential products

for p in products:           #have to separate functions because the execute command only executes first line
    print (p["name"])

print ("-----------------------")
print ("There are " + str (len (products)) + " products:")    # good sample of how to embed function within functon; "cancatanate strings" with '+' sign
print ("-----------------------")                           # str function changes a variable to string so can cancatanate strings

def sort_by_name (p):               # Understand this
    return p ["name"]
products = sorted (products, key = sort_by_name)

for p in products:           #cancatanate strings
    print ("$*$ " + p["name"])

for p in products:
    price_format = '${0:.2f}'.format(p["price"])              # use separate area to construct price: $ sign, have 2 decimal points etc.
    print ("$*$ " + p["name"] + " " + "(" + price_format + ")")

dept = []      #created new empty list called department
for p in products:
    dept.append(p["department"])         #appended departments list to empty list

dept = set (dept)                   #change list to set to list so we can take out duplicates
dept = list (dept)

print ("-----------------------")
print ("There are " + str (len (dept)) + " departments:")
print ("-----------------------")

for d in sorted(dept):                                    #creating another for loop that can sort_by_name
    print ("$*$ " + d.title())                          #.title changes case to title case
    # print ("$*$ " + d.title() + "(" + "X products" + ")")

def product_belonging_to (dept_name):
    return [p for p in products if p["department"] == dept_name]                                    #list comprehensions

for d in dept: 
