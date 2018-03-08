nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# make a new list with each n in nums
my_nums = []
for n in nums:
    my_nums.append(n)

print(my_nums)

# COMPREHENSION VERSION
compre_nums = [n for n in nums]
print(compre_nums)

# make a new list with each n squared in nums
my_nums = []
for n in nums:
    n = n * n
    my_nums.append(n)

print(my_nums)

# COMPREHENSION VERSION
compre_nums = [n * n for n in nums]
print(compre_nums)

# MAP & LAMBDA VERSION
my_sqaured_nums = map(lambda n: n * n, my_nums)
for n in my_sqaured_nums:
    print(n)

# make a list of even numbers
all_nums = [1, 2, 494, 23, 9939, 28]

evens_only = []
for n in all_nums:
    if n % 2 == 0:
        evens_only.append(n)
print(evens_only)

# Comprehension
evens_only = [n for n in all_nums if n % 2 == 0]
print(evens_only)

# filter & lambda
evens_only = filter(lambda n: n % 2 == 0, all_nums)
print(evens_only)

# make list of tuples
# [(0, a), (1, b), ...]
letters = ['a', 'b', 'c', 'd', 'e']
nums = [1, 2, 3, 4, 5, 6]

new_list = []
for n in nums:
    for l in letters:
        new_list.append((n, l))
print(new_list)

print('-+-!' * 20)
# comprehension
my_list_of_tuples = [(n, l) for n in nums for l in letters]
print(my_list_of_tuples)

print('+-!' * 20)

# Dictionary Comprehension
names = ['jakkrit', 'bruce', 'clark', 'pete']
heros = ['pigman', 'batman', 'superman', 'wolverine']
print(zip(names, heros))

# make a dict {'name': 'hero'}
my_dict = {}
for name, hero in zip(names, heros):
    my_dict[name] = hero

print(my_dict)

# comprehension
my_dict = {name: hero for name, hero in zip(names, heros) if name == 'jakkrit'}
print(my_dict)
