# Define the function `subsett` with parameters `nums` and `s`
def subsett(nums, s):
    result = []  # Initialize an empty list to store subsets that sum to `s`
    subset = []  # Initialize an empty list to store the current subset being explored

    s = 3  # the value subsets would have to align with 
    
    # Define a recursive function `dfs` to explore subsets
    def dfs(i):
        # Check if the current subset `subset` has at least one element
        if len(subset) >= 1:
            # Calculate the sum of elements in the current subset `subset`
            d = sum(subset)
            print(d)  # Print the sum for debugging purposes

            # Check if the sum of elements in `subset` equals `s`
            if d == s:
                # If the sum equals `s`, add a copy of `subset` to `result`
                result.append(subset.copy())
                return  # Exit the current recursive call

            # Check if the sum of elements in `subset` exceeds `s`
            if d > s:
                return  # Exit the current recursive call

        # Check if all elements in `nums` have been explored
        if i >= len(nums):
            return  # Exit the current recursive call

        # Include the current element `nums[i]` in the subset
        subset.append(nums[i])
        # Recursively explore subsets including `nums[i]`
        dfs(i + 1)

        # Exclude the current element `nums[i]` from the subset
        subset.pop()
        # Recursively explore subsets excluding `nums[i]`
        dfs(i + 1)

    # Start exploring subsets from the first element of `nums`
    dfs(0)

    # Check if any subsets sum to `s`
    if len(result) > 0:
        return True  # Return True if at least one subset sums to `s`
    else:
        return False  # Return False if no subset sums to `s`

# Define the list `nums` and the target sum `s`
nums = [1, 2, 3]
s = 3
# Call the function `subsett` with `nums` and `s`, and store the result in `d`
d = subsett(nums, s)
# Print the result `d`
print(d)