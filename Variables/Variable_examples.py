#Day 2 Tasks:

#A variable is like a container which holds information
#It's called a variable because the value inside can vary, it's not fixed or constant

#setting variables:

num = 5 #setting a variable with a number value
decimal = 5.4 #setting a variable with a decimal value
name = "Ambia" # setting a variable with a string value

#using == compares to check if two things are equal whereas = assigns a variable a value

#printing all three values which are associated with these variables
print (num)
print (decimal)
print (name)


#Strong vs Weak typed language
# A strongly typed language: doesn't allow mixed data types to be used together (e.g. int and string)
#Example: "5" + 3 --> would print an error because a string and int are of different data types

# Weakly typed: automatically converts the data type of the variable (e.g. int to string conversion)
#Example: "5" + 3 --> this would print 53 bc the int value is automatically converted to a string


#Dynamic vs Static languages

#Dynamically typed language: A language where the type doesn't have to be declared before the variable
#Exmaple:
#name = "Ambia" #although my name is of string type, it doesn't need to be declared because python knows it's a string from the "" marks

#Statically typed language: A language where tht type needs to be delcared or complier error
#Exmaple:
#str name = "Ambia"  # type needs to be declared before setting the value to the variable


#Id() Fucntion:

#id(): built in python function that shows where a variable is stored in the computers memory
#Code example:
age = 21
print(id(age)) #shows memory address of variable ID
age = 22
print(id(age))  #shows a different memory address of the variable ID
#Python creates a new object (value) rather than modifying the old one

#Code Example:
x = 10
y = x 
print(id(x))
#The id of x and y is the same as both variables point to the same object (so both = 10 )
#If the value of x changes, y still keeps the original ID and x has a new one
#x points to a new object while y still points to the old one x was assigned to


#Assigning one Variable to another
name = input("Enter your name") # get users names
age =  int(input("Enter your age: "))
dob =  input("Enter your date of birth: ") #get age and DOB

name = input("Enter your name: ")
print ("Hi", name)
