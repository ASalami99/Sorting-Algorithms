def get_min_value(d):
    min_value = float('inf')
    for x in d:
        for y in d:
            if y < x and y < min_value:
                min_value = y
    return min_value

d = [80,67,12,56,7,8,9,0]
print(get_min_value(d))


#min_value = float('inf')
# def get_min_value_2(d):
#     min_value = 0
#     for x in d:
#         if(min_value > x):
#             min_value = x
#     return min_value

# d = [80,67,12,56,7,8,9,-1]
# print(get_min_value_2(d))