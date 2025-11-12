
#Day 2 Tasks

#Data Types and Operators
#An operator is a symbol that tells te computer what operation to perform
#An operand is the value or variable that the operator acts upon
#e.g. 5 + 3 --> + is the operator, 5 and 3 are the operands

#Understanding different types of operators
num1 = 13
num2 = 6

print(num1 + num2)  #addition
print(num1 - num2)   #subtraction
print(num1 * num2)  #multiplication
print(num1 / num2)  #divison
print(num1 % num2) #remainder of divison

#understading comparison operators
num3 = 10
num4 = 15

print(num4>num3) # num4 is greater than num3
print(num3<num4) # num3 is less than num4
print(num3==num4) # is num3 equal to num4
print(num3!=num4) # check if num3 is not equal to num4
print(num4>=num3) #num4 is greater than or equal to num3
print(num4<=num3) #num3 is less than or equal to num4



#Strings and quotes

#bad_string = 'I said 'Wow!''
#print(bad_string) # Fails because python thinks the quote ended before the word Wow

# Three types of fixes
bad_string = 'I said \'wow!\'' # Escape single quotes
print(bad_string)
bad_string = "I said 'Wow!'" #double quotation marks
print(bad_string)
bad_string = '''I said 'Wow!' ''' #triple single quotation marks
print(bad_string)
bad_string = 'I said "Wow!"' #double quotation marks
print(bad_string)


#Slicing:
# slicing strings lets your pick a part of a string
# starts from index 0 for positive indexes
# starts from -1 for negative indexes

#How Slicing works:
#[start:stop] --> which index to start at and what index to stop by but not print
#[start: ] --> from start index chosen to end
#[:stop ] --> from the start until chosen index


Hw = "Hello world!"
print(Hw)

# 11 total characters including space and exclamation mark
# H e l l o   W o r l d  !
# 0 1 2 3 4 5 6 7 8 9 10 11

# Get the character in the first position
print(Hw[0]) #start and stop indexes are the same

#Get the last character
print(Hw[-1])

# Get the 2nd last character
print(Hw[-2])

# Write a comment to EXPLAIN what does this do
print(Hw[2:]) #this retrieves the indexes 2 to the end of the string (2 to 11)

# Write a comment to EXPLAIN what does this do
print(Hw[-3:]) # this retrieves the indexes -3 (third last letter) and prints till the end of the string

# Write a comment to EXPLAIN what does this do
print(Hw[:5]) #this retrieves indexes up until 5 but doesn't print thr 5th index

# Starts from the second,  (doesn't include it)
print(Hw[1:4]) #starts from the second index and stops at the 5th but doesn't include it

#Consolidation tasks: Guessing game wth string slicing
original_word = "recommendation"
scrambled_word = "eoommandretnic"

print("Scrambled word:", scrambled_word) #Showing the user the scrambled word
print("Guess the original word from the scrambled version.")
print("Here are some hints:")

hint1_slice = original_word[4:5]
hint2_slice = original_word[11:14]
hint3_slice = original_word[7:10]
hint4_slice = original_word[0:1] # setting the hints through slicing

print("Hint 1 (Letter at index 4):", hint1_slice)
print("Hint 2 (Letters at index 11-13):", hint2_slice)
print("Hint 3 (Letters at index 7-9):", hint3_slice)
print("Hint 4 (Letter at index 0):", hint4_slice) #showing the user the hints

print("What's your guess?")


#Convert/Casting

# Write comment to explain what this does:
str_with_extra_spaces = "   extra spaces at the start and end    "  #formats the variable to have extra spaces at the start and end of the string


# Write comment to explain what this does
print(len(str_with_extra_spaces)) #tells us the length of string using len function

#correct method to remove extra space
print(len(str_with_extra_spaces.strip())) # in order to remove unwanted spaces at the start / end



example_text = "here's some text with some words of text"
# count how many times the substring 'text' occurs within example_text & print it to the screen
print(example_text.count("text"))

# convert example_text to lowercase & print it to the screen
print(example_text.lower())

# convert example_text to uppercase & print it to the screen
print(example_text.upper())

# capitalise the first letter in example_text & print it to the screen
print(example_text.capitalize())

# replace the word 'with' in example_text with a comma (,)instead & print it to the screen
print(example_text.replace("with",  ","))
# old and new string both require their own set of quotation marks


#concatination: joining strings together
x = 2
y = 5.4
z = " there's now a number 25.4 unless we put a space in!"
#print(x + y + z)  This will not work (cant concatinate int and string, only strings)

z = " theres now a number " + str(x) + " "  + " " + str(y) + " unless we put a space in!"
print(z) #will print bc x and y have been converted from ints to strings


#f-string: a way to use variables with text
name = "Lassie"
years = 7
height_cm = 60.2
print(f" {name} is {years} years old and {height_cm} tall")


#Starting code:
pi = 3.14159265359
# Use an f-string to print pi to 3 decimal places e.g. 'Pi to 3 decimal places: <value>'
print(f"Pi to 3 decimal places: {pi:.3f}") #.f means a num of decimal places for regular numbers

# Use an f-string to print pi to 5 decimal places e.g. 'Pi to 5 decimal places: <value>'
print(f"Pi to 5 decimal places: {pi:.5f}")

score = 16
max_score = 26
score_as_decimal = score/max_score

# Use an f-string to print 'score_as_decimal' e.g. 'You scored 0.6153846153846154' (no % sign)
print(f"you scored  {score_as_decimal}")

# Use an f-string to print 'score_as_decimal' formatted as a percentage e.g. 'You scored 61.538462%'
print(f"you scored {score_as_decimal*100}") #multiply by 100 to get percentage

# Use an f-string to print 'score_as_decimal' formatted as a percentage to rounded to 2 decimal places e.g. 'You scored 61.54%'
print(f"you scored {score_as_decimal: .2%}") #percentage with 2 decimal places (multiplied by 100 and adds%)

# Use an f-string to print 'score_as_decimal' formatted as  percentage to rounded to a whole number e.g. 'You scored 62%'
print(f"you scored {score_as_decimal: .0%}")#percentage with 0 decimal places, rounded to whole number








