# word = input("Enter a string: ")
# if word[::-1] == word:
#     print("This is a palindrome!")
# else:
#     print("This is not a palindrome!")


from collections import deque

def palindrome_checker(the_string):
    itis_palindrome_checker = True
    string_to_check = deque(the_string)
    while(len(string_to_check)>= 2):
        left_character = string_to_check.popleft()
        right_character = string_to_check.pop()

        if (left_character != right_character):
            itis_palindrome_checker = False

    return itis_palindrome_checker

print(palindrome_checker("racecar"))

   

