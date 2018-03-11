# create list of squares with normal for loop
list_of_nums = [1, 3, 4, 6, 9]


def square_numbers(nums):
    squares = []
    for num in nums:
        squares.append(num * num)
    print(squares)


square_numbers(list_of_nums)

print('*'*40)


# to create generator, just yield the result
def square_generator(nums):
    for num in nums:
        yield (num * num)


# generator doesnt compute anything
# you just have to call next() to yield each result
my_nums = square_generator(list_of_nums)

print(next(my_nums))
print(next(my_nums))

# to prevent index error, put it in the for loop
for num in my_nums:
    print(num)

print('*'*30)

# same result can be expressed by list comprehension
# you will lose generator performance
list_comp = [n*n for n in list_of_nums]
print(list_comp)

print('+!+'*20)

# generator can be used by replaced [] with ()
list_gen = (n*n for n in list_of_nums)
# print(next(list_gen))
# print(next(list_gen))
# print(next(list_gen))
# print(next(list_gen))
# print(next(list_gen))
#
# print('+!+'*20)

# or
for i in list_gen:
    print(f'this is gen: {i}')

# you can cast it to a list but losing performance
# print(list(list_gen))