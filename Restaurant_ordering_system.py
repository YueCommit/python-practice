# display welcome
print("Welcome to Python Burger! Here is our menu with prices:")
#  initiate menu dictionary
menu = {
   1: {"name": "burger", "price": 5.99},
   2: {"name": "pizza", "price": 8.49},
   3: {"name": "salad", "price": 4.99},
   4: {"name": "drink", "price": 1.99}
}

#final order total value
item_total = 0
order = {}
#print menu with number, name and price
for item_number, details in menu.items():
    print(f"{item_number}. {details['name']}, ${details['price']}")
while True:
    # Prompt menu selection
    item_choice = int(input("Choose menu item: "))
    # Prompt quantity
    if item_choice in menu:
        item_qty = int(input("How many would you like to order? "))
        item_name = menu[item_choice]['name']
        #adding chosen menu item price to running total
        #item_total += menu[item_choice]['price'] * item_qty
        if item_name in order:
            order[item_name] += item_qty
        else:
            order[item_name] = item_qty
    else:
        print("That is an invalid answer!")
    # prompt user if they would like to continue ordering
    continue_ordering = input("Would you like to order anything else? (yes/no): ").strip().lower()
    if continue_ordering != 'yes':
        print(f"Your final order is: {order}")
        break

#calculating total outside of loop
name_to_price = {item['name']: item['price'] for item in menu.values()}
for item_name, qty in order.items():
    price = name_to_price[item_name]
    line_total = price * qty
    item_total += line_total
    print(f"{item_name}: {qty} = ${line_total:.2f}")
print(f"Grand Total: ${item_total:.2f}")


# # Initiate WHILE loop
# while True:
#     # display menu items
#     #  Display menu items - (print statement) - for loop initiate menu_items
#     print("Item | Name | Price")
#     print("1.   Burger | $5.99")
#     print("2.   Pizza  | $8.49")
#     print("3.   Salad  | $4.99")
#     print("4.   Drink  | $1.99")


# # STOP HERE

# # add to order
# ability for cust. to add mult qty of items from menu to order
# Add to order - fn
# order += item_choice
# order += item_quantity



# # continue order
# Continue ordering? yes/no
# boolean - y/n to break while loop 
# If yes, return
# If no, break loop <- end of loop
# # calculate total

# for i in customer_order
# 	item_total = 

# print/calculate final total (to two .pt)
# Final total - items + price/total? - for loop
# Order confirm true/false ^


# # display menu items
# Item number		name of item		price
# 1				Burger			$5.99
# 2				Pizza				$8.49
# 3				Salad				$4.99
# 4				Drink				$1.99