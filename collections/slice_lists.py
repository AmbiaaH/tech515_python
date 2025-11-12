#Day 3 Task 3

mixture = [1, 2, 3,"one", "two", "three"]
print(mixture)
print(mixture[1:3]) #returns 2nd and 3rd items in list using slicing

print(mixture[0:5:2])#returns every second number

#NOTES:
#start → where slicing begins (index)
#end → where it stops (non-inclusive)
#step → how much the index increases each time

print(mixture[-1:3:-1]) # returns last two items in list by starting at end of list, stopping at 3rd item and stepping in reverse