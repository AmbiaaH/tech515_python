#Day 3 Task 5:
#each value needs to be accompanied by a key, the format of dictionaries is : {key:value}

student_1 = {
    "name": "susan",
    "stream": "tech",
    "completed_lessons": 4,
    "completed_lessons_names": ["variables", "data_types", "set up"]}
print(student_1)
print(type(student_1)) #data type of dictionary
print(student_1["stream"]) # value pairing to key stream
print(student_1["completed_lessons_names"]) # all three values printed
print(type(student_1["completed_lessons_names"]))
print(student_1["completed_lessons_names"][0])

#NOTE:Two sets of square brackets [key name]: [value index for printing]

student_1["completed_lessons"] = 3 #change value of completed lessons key to 3
student_1["completed_lessons_names"].remove("variables")
print(student_1)

#Note: to use remove [key].remove(value)

student_1.keys()


