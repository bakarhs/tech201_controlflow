# Looping

# A For loop is where you define an iterator number and cycle through data (list/ dictioanry) 'foreach' entry in the data structure.

# Creating a for loop

list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1, 2, 3],[4, 5, 6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}}

# for num in list_data:
#     print(num * 2)


# Nested for loop

# for data in embedded_lists:
#     print (data)
#     for num in data:
#         print(num)

# loops for dictionaries

# for item in dict_data.values:
#     print(item)

for item in dict_data.values():
    for embed_value in item.values():
        print(embed_value)

for items in dict_data.values():
    print(items["money"])

# please see python documentation for more you can do with dictionaries and loops.

# Loops and if statments

list_1 = [1, 2, 3, 4, 5]

for num in list_1:
    if num == 3:
        print("I found 3")
    elif num > 3:
        print("Gone too far!")
    else:
        print("Too soon")

