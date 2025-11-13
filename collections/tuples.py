#Day 3 Task 4:

#Tuples and lists can both store multiple types of items (int,str,float)
#Tuples are immutable as they cant be changed once created unlike lists
#Python data types: string, int, float, booleans etc : e.g. Hello cant be changed to yello but modifying index[0]
#Tuples are good for fixed data that shouldn't change, something hashable or for protected data
#.count method counts how many times bread appears in the tuple



#DESERT ISLAND GAME:


print("You are stranded on a desert island. You can take only THREE items.")
essential_item1 = input("What is an essential item you would take? ")
essential_item2 = input("What is an essential item you would take? ")
essential_item3 = input("What is an essential item you would take? ")

essentials_tuple = (essential_item1, essential_item2,  essential_item3) #Tuple with user input

print("Here are your items as a tuple:", essentials_tuple)
print("")
print("I lied. You can take one more item.")


essential_item4 = input("What is one more essential item you would take? ") #create new essential variable to store 4th essential
extended_essential_tuple = (essentials_tuple, essential_item4) #put original tuple and new essential item as one under extra_essential_tuple variable
print("Here are your items with the 4th tuple item added ",  extended_essential_tuple) #print both together 




