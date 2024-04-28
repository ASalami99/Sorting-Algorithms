def insert_sort(array):
    for i in range(1,len(array)):
        j = i
        while(array[j-1]> array[j] and j>0):
            array[j], array[j-1] = array[j-1], array[j]
            j = j-1

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insert_sort(a_list)
print(a_list)