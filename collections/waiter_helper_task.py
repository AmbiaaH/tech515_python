#level 1
starters = ['chips', 'garlic bread','halloumi sticks', 'mixed olives', 'calamari']
main = ['margarita pizza ', 'sausage pizza', 'pineapple pizza', 'vegeterian pizza']
desserts = ['ice cream', 'chocolate cake', 'tiramisu']


print("Hello user")

print("Please choose a starter: ",starters)
starter_choice = input()

print("please choose a main: ", main)
main_choice = input()

print("please choose a dessert: ", desserts)
dessert_choice = input()

final_choice = (starter_choice, main_choice, dessert_choice)

print("Here are your meal choices: ", final_choice)



#level 2 f string
starters = ['chips', 'garlic bread','halloumi sticks', 'mixed olives', 'calamari']
main = ['margarita pizza ', 'sausage pizza', 'pineapple pizza', 'vegetarian pizza']
desserts = ['ice cream', 'chocolate cake', 'tiramisu']

customer_order_list = [] #

print("Hello user")

print(f"Please choose a starter: {starters}")
starter_choice = input()
customer_order_list.append(starter_choice)

print(f"please choose a main: { main} ")
main_choice = input()
customer_order_list.append(main_choice)



print(f"please choose a dessert:  {desserts}")
dessert_choice = input()
customer_order_list.append(dessert_choice)

print("Here are your meal choices: ", customer_order_list)
