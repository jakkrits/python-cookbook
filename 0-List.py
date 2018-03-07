# LISTS ARE MUTABLE
# TUPLES ARE IMMUTABLE
courses = ['ying', 'nan', 'buffy']
new_courses = ['fon', 'kwnag', 'boom']

courses.append('chiro')
print(courses)

courses.insert(0, new_courses)
print(courses)

del courses[0]
print(courses)

print('*'*50)

courses.extend(new_courses)
print(courses)

print('-'*50)

courses.remove('kwnag')
print(courses)

popped = courses.pop() # pop removes the last item and also returns that popped value
print(courses)
print(popped)

# revese list
courses.reverse()
print(courses)

# sort
courses.sort()
print(courses)

courses.sort(reverse=True)
print(courses)

print('*' * 60)

# sort without mutating original
new_sorted = sorted(courses)
print(new_sorted)
print(courses)

print('#' * 100)

nums = [1, 200, 309, 30, 82, 203, 488]
print(min(nums))
print(max(nums))

print('--' * 20)

# find index
print(nums.index(203))
print(courses.index('chiro'))

# find if value is in the list
print('fon' in courses)

print('*+' * 25)

# loop through the list
for name in courses:
    print(name)

# for loop with index & value
for index, name in enumerate(courses):
    print(f'index: {index} - name: {name}')

print('-*' * 25)

# enumerate with start index
for index, name in enumerate(courses, start=1):
    print(f'index: {index} - name: {name}')

print('+-' * 25)

# convert list to a string using JOIN
course_string = ','.join(courses)
print(course_string)
course_string = ' ,'.join(courses).title()
print(course_string)

# create list from strings using SPLIT
converted_list = course_string.upper().split(' ,')
print(converted_list)