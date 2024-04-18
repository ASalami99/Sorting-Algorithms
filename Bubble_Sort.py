def bubble_sort(the_list):

    for scope in range(len(the_list)-1,0,-1):
        for i in range(scope):
            #Method 1: Swapping
            if (the_list[i] > the_list[i+1]):
                the_list[i], the_list[i+1] = the_list[i+1], the_list[i]
            #Method 2: Storing it in a new variable
            if(the_list[i] > the_list[i+1]):
                tem = the_list[i]
                the_list[1] = the_list[i+1]
                the_list[i+1] = tem


#Time comlexity is always n^2

l = [4,1,6,20,2,5]
bubble_sort(l)

print(l)
    