def selection_sort(the_list):

    for slot_to_fill in range(len(the_list)-1,0,-1):
        position_of_max = 0

        for i in range(1, slot_to_fill+1):
            if (the_list[position_of_max] < the_list[i]):
                position_of_max = i
                
        the_list[slot_to_fill], the_list[position_of_max] = the_list[position_of_max], the_list[slot_to_fill]



l = [45,67,8,9,0,-12,5]
selection_sort(l)

print(l)