'''
CIS 129 - Lab 03: Coffee Shop
Author: Armando Lopez
Date: 02/17/25
Creating a reciept for Alo's Coffee Shop based on how many items customer's purchase
'''


# create structure, add menu items and assign value
print('***************************************') # reciept line
print("Alo's Coffee Shop") # shop name top of reciept
coffee = 5.00 # coffee price is five dollars
muffin = 4.00 # muffin price is four dollars
smoothie = 6.00 # smoothie price is six dollars
burrito = 8.00 # burrito price is eight dollars


# user input information
coffee_input = int(input('Number of coffees bought? ')) # prompts user
print(coffee_input) # prints out amount of coffees purchased

muffin_input = int(input('Number of muffins bought? ')) # prompts user
print(muffin_input) # prints out amount of muffins purchased

smoothie_input = int(input('Number of smoothies bought? ')) # prompts user
print(smoothie_input) # prints out amount of muffins purchased

burrito_input = int(input('Number of burritos bought? ')) # prompts user
print(burrito_input) # prints out amount of burritos purchased


# reciept structure
print('***************************************') # reciept line
print() # space between line
print() # space between line
print('***************************************') # reciept line


# title
print("Alo's Coffee Shop")


# calculation for coffees
if coffee_input == 1: # verifies quantity
    print(coffee_input , 'Coffee at $5 each: $ ', coffee) # output singular
else:
    print(coffee_input , 'Coffees at $5 each: $ ', coffee * coffee_input) # output plural
    
    
# calculation for muffins
if muffin_input == 1: # verfies quantity
    print(muffin_input , 'Muffin at $4 each: $ ', muffin) # output singular
else:
    print(muffin_input , 'Muffins at $4 each: $ ', muffin * muffin_input) # output plural
    
# calculation for smoothies
if smoothie_input == 1: # verifies quantity
    print(smoothie_input , 'Smoothie at $6 each: $ ', smoothie) # output singular
else:
    print(smoothie_input , 'Smoothies at $6 each: $ ', smoothie * smoothie_input) # output plural


# calculation for burritos
if burrito_input == 1: # verifies quantity
    print(burrito_input , 'Burrito at $8 each: $ ', burrito) # output singular
else:
    print(burrito_input , 'Burritos at $8 each: $ ', burrito * burrito_input) # output plural


# totals
coffee_total = int(coffee * coffee_input)
muffin_total = int(muffin * muffin_input)
smoothie_total = int(smoothie * smoothie_input)
burrito_total = int(burrito * burrito_input)

cost = coffee_total + muffin_total + smoothie_total + burrito_total


# calculation of taxes and total
tax = 0.06 * cost
total = cost + tax


# prints out order calculations
print('6% tax: $', tax)
print('---------')
print('Total: $', total)

print('***************************************')

# thank you message for customer
print("Thank you for visiting! Come back soon!")
