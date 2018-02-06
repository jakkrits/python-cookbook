from collections import deque

q = deque(maxlen=3)
print(q)
q.append(10)
q.append(20)
q.append(390)
print(q)
q.append(11)
print(q)