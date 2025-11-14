list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1,2,3],[4,5,6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}}

# 1. loop through a list

for num in list_data:
    num = num * 2
    print(num)

# 2. loop through a nested list

for data in embedded_lists: #data is the items within the list which is each list embedded in the main list
    print(data)
