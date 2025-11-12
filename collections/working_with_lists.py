# Day 3 Task 1:

shopping_list = ['eggs', 'bread', 'bananas', 'biscuits', 'milk'] #creating list
print(shopping_list) #printing list

type(shopping_list) #bult in type method
print(type(shopping_list)) #use method type with variable and print

print(shopping_list[0]) #print first item in list
print(shopping_list[4]) #print last item in list

shopping_list[1] = 'rice'#modifying list, replacing bread with rice
print(shopping_list)

shopping_list.append('carrots') #appending list by adding carrots
print(len(shopping_list)) #using len method to check length of list after update

shopping_list.extend(['toffee', 'coffee']) #extend method to add multiple items to list
print(shopping_list)
print(len(shopping_list))

shopping_list.remove('bananas') #remove method to remove item from list
print(shopping_list)

shopping_list.pop(6) #pop method to remove last item from list
print(shopping_list)






