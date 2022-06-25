
# Error. 1.
# error message requires get_pet_shop_name to be defined. 
# def get_pet_shop_name using dictionary key. 

def get_pet_shop_name(shop):
    return shop["name"]

# Error. 2.
# error message requires get_total_cash to be defined.
# def using the two dictionary keys admin & total cash. 

def get_total_cash(shop):
    return shop["admin"]["total_cash"]

# Error. 3. 
# add_or_remove_cash requires definition. 
# Def wants 10 added to admin>total cash eg. cash 
# From failed tests I ascertained it needs 2 arguments & parameters.
# Add 10 to the get_total_cash function- access shop as before. 

def add_or_remove_cash(shop, money):
    shop["admin"]["total_cash"] += money

# Entry 4-
# Initally thought this would be same as prior with -, but func already def so user will calc if -.

# Error 5 
# get_pets_sold requires definition. 
# Use the two dictionary keys admin and pets_sold.

def get_pets_sold(sales):
    return sales["admin"]["pets_sold"]

# Error 6 
# increase_pets_sold requires definition
# Similar to error 3, increase the get_pets_sold. No return is required as no =

def increase_pets_sold(sales, pets):
    sales["admin"]["pets_sold"] += pets





    






