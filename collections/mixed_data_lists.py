#Day 3 Task 2
name = input("Enter your name: ") # get users names
age =  int(input("Enter your age: "))
dob =  input("Enter your date of birth: ")

user_details_list = [name, age, dob]
print (user_details_list[0])
#NOTE: when accessing and modifying an item use the index
#NOTE: when adding new items use the value itself

print(user_details_list) # print entire list with user input

height = float(input("Enter your height in cm : "))
(user_details_list.append(height))
print(user_details_list)

