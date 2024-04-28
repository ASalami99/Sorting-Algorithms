#Stack Operations

# s = []
# s.append(3)
# s.append("dog")
# print(s[0])
# s.append(True)
# print(len(s))
# s.append(8.4)
# s.pop()
# print(s)
# s.pop()
# print(s)
# s.append(45)
# s.append(6)
# s.pop()
# s.pop()
# s.pop()
# s.insert(0,2)
# print(s)
# s.pop(0)
# print(s)    


# m = []
# m.append('x')
# m.append('y')
# m.append('z')
# while len(m) >0:
#     m.pop()
#     m.pop()
# print(m)


def rev_string(s):
    stack = list(s)
    stack2 = []
    while len(stack) >0:
        stack2.append(stack.pop())
    answer = '' .join(stack2)
    return answer

print(rev_string("James"))



