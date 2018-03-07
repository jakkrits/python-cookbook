student = {'name': 'John', 'age': 28, 'courses': ['math', 'compsci']}
print(student)

print(student['courses'][0])

# keys can be any immutable data type
int_key_dict = {32: 'thirty two'}
print(int_key_dict[32])

# getting error if accessing invalid key
# print(student['not exist'])

# use GET method to prevent error or to return default

print(student.get('phone number'))
print(student.get('phone number', 'Not Exist')) # return default if not exist

# add new entry
student['phone number'] = '888-888-8888'
print(student.get('phone number', 'Not Exist'))

# if the key exists, we can update it
student['name'] = 'Jane'
print(student)

# use UPDATE method to add and/or update
student.update({'name': 'ควย', 'age': '99', 'phone numbers': '999-999-9999'})
print(student) # updated and changed data type on 'age' key and added new 'phone numbers' key

print('!+' * 25)

# delete using DEL
del student['phone numbers']
print(student)

# delete using POP return 'VALUE'
popped = student.pop('age')
print(student)
print(popped)

# delete using popitem return (KEY, VALUE)
key, value = student.popitem()
print(f'key: {key}, value: {value}')
print(student)

# show length
print(len(student))

# list keys
print(student.keys())

# list values
print(student.values())

# list key value pairs
print(student.items())

# loop through the keys
for key in student:
    print(key)

# loop thrugh keys and values
for key, value in student.items():
    print(f'{key}, and {value}')