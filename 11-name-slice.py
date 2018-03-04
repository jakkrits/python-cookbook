items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print(items[a])

items[a] = [111, 222]
print(items)

del items[a]
print(items)

a = slice(2, 10, 3)
print(a.start)
print(a.stop)
print(a.step)

print('*' * 20)

# map a slice onto a sequence of a specific size by using its indi
# ces(size) method. This returns a tuple(start, stop, step)
s = 'helloWORLD'
a.indices(len(s))
for i in range(*a.indices(len(s))):
    print(s[i])

print(a.indices(len(s)))
print(*a.indices(len(s)))
