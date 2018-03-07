# extract or reduce the sequence using criteria

mylist = [1, 4, -5, 10, -7, 2, 3, -1]

# use list comprehension
n_more_than_zero_list = [n for n in mylist if n > 0]
print(n_more_than_zero_list)

n_less_than_zero = [n for n in mylist if n < 0]
print(n_less_than_zero)