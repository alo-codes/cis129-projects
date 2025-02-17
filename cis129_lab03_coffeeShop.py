'''Creating a reciept for My Coffee and Muffin Shop based on how many items customer's purchase'''

# create structure, add menu items and assign value
print('***************************************') # reciept line
print('My Coffee and Muffin Shop') # shop name top of reciept
coffee = 5.00 # coffee price is five dollars
muffin = 4.00 # muffin price is four dollars

# user input information
coffee_input = int(input('Number of coffees bought? ')) # prompts user
print(coffee_input) # prints out amount of coffees purchased

muffin_input = int(input('Number of muffins bought? ')) # prompts user
print(muffin_input) # prints out amount of muffins purchased

# reciept structure
print('***************************************') # reciept line
print() # space in between line
print() # space in between line
print('***************************************') # reciept line

# title
print('My Coffee and Muffin Shop Receipt')

# calculation for coffees
if coffee_input == 1: # verifies quantity
    print(coffee_input , 'Coffee at $5 each: $ ', coffee) # output singular
else:
    print(coffee_input , 'Coffees at $5 each: $ ', coffee * coffee_input) # output plural
    
# calculation for muffins
if muffin_input == 1: # verfies quantity
    print(muffin_input , 'Coffee at $4 each: $ ', muffin) # output singular
else:
    print(muffin_input , 'Coffees at $4 each: $ ', muffin * muffin_input) # output plural
    
# totals
coffee_total = int(coffee * coffee_input)
muffin_total = int(muffin * muffin_input)

cost = coffee_total + muffin_total

# calculation of taxes and total
tax = 0.06 * cost
total = cost + tax

# prints out order calculations
print('6% tax: $', tax)
print('---------')
print('Total: $', total)
print('***************************************')
