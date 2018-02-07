from collections import defaultdict

d = defaultdict(list)
d['key_a'].append(1)
d['key_a'].append(2)
d['key_a'].append(3)
d['key_b'].append(4)

print(d)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['a'].add(3)
d['b'].add(4)

print(d)

di = {}  # A regular dictionary
di.setdefault('a', []).append(1)
di.setdefault('a', []).append(2)
di.setdefault('b', []).append(4)
# make d a default dict without behavior
# One caution with defaultdict is that it will automatically create dictionary entries for
# keys accessed later on(even if they aren’t currently found in the dictionary). If you don’t
# want this behavior, you might use setdefault() on an ordinary dictionary instead.

print('*' * 30)

# defaultDict preserves order
for key in d:
    print(key, d[key])
print('*' * 30)
for key, value in d.items():
    print(key, value)