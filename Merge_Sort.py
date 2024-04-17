def merge_sort(the_list):

    if (len(the_list) > 1):
        mid = len(the_list)//2
        left = the_list[:mid]
        right = the_list[mid:]
        merge_sort(left)
        merge_sort(right)

        l = 0
        r = 0
        c = 0

        while (l < len(left) and r < len(right)):
            if left[l] < right[r]:
                the_list[c] = left[l]
                c = c + 1
                l = l + 1

            else:
                the_list[c] = right[r]
                c = c + 1
                r = r + 1

        while (l < len(left)):
            the_list[c] = left[l]
            c + c + 1
            l = l + 1

        while (r < len(right)):
            the_list[c] = right[r]
            c = c + 1
            r = r + 1

nums1 = [20,5,4]
nums1 = [20,4,5,40,10,998,867]
merge_sort(nums1)
print(nums1)

#nums1 = [20,4,5,40,10]
#complexity = n logn  (better than n^2)
