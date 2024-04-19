def BS(the_list, number_to_find):

    l = 0
    r = len(the_list)-1
   # print(len(the_list))
    found = False

    while(l <= r and found == False):
        mid_point = (l + r)//2

        if(the_list[mid_point] == number_to_find): 
            found = True
        else:
            if(number_to_find > the_list[mid_point]):
                l = mid_point + 1
            else: r = mid_point -1

    return found

print(BS( [4,6,8,10,12], 14))
