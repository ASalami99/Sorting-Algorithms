# d = [80,67,12,56,7,8,9,0]

# def finder(the_value_to_find):
#     for element in d:
#         if(element == the_value_to_find):
#             return True
#     return False

# print(finder(99))

d = [0,7,8,9,12,67,80]

def finder(the_value_to_find):
    counter = 0
    for x in d:
        if(x == the_value_to_find):
            return True
        if(x > the_value_to_find):
            return False

        counter = counter + 1
    return False

print(finder(99))