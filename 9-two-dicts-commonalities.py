a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

# find keys in common
# remember ordinary dict is not ordered
common_keys = a.keys() & b.keys()
print(common_keys)

# find keys in a but not in b
only_in_a = a.keys() - b.keys()
print(only_in_a)

# Find (key,value) pairs in common
common_key_value = a.items() & b.items()  # { ('y', 2) }
print(common_key_value)

# Make a new dictionary with certain keys removed
c = {key:a[key] for key in a.keys() - {'y', 'z'}}
print(c)
