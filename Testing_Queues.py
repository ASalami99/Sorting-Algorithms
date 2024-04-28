from collections import deque

d = deque()

print(len(d))
d.append(3)
d.append(4)
d.popleft()
d.append("Hello Boys")
d.insert(0, 37)
print(d)