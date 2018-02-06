'''
1.1. Unpacking a Sequence into Separate Variables
'''
p = (4, 5)
print(type(p))
x, y = p
print(x, y)

data = ['ME', 50, 91.1, (2012, 12, 31)]
name, age, height, year = data
print(year)
name, age, height, (year, month, day) = data
print(day)

'''
1.2. Unpacking Elements from Iterables of Arbitrary
Length
'''
def print_middle_grade(grades):
    first, *middle, last = grades
    print(*middle)

grades = [1,22222,3,4,5,6,7, 8, 8, 99, 92222, 10]
print_middle_grade(grades)

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
first_name, email, *phone_numbers = record
print(phone_numbers)
print(type(phone_numbers))

phone1, phone2 = phone_numbers
print(phone2)

# Avg all previous sales records
# *trailing_qtrs, current_qtr = sales_record
# trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)
# return avg_comparison(trailing_avg, current_qtr)

records = [
('foo', 1, 2),
('bar', 'hello'),
('foo', 3, 4),
]
def do_foo(x, y):
    print('foo', x, y)
def do_bar(s):
    print('bar', s)
for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *field, homedir, sh = line.split(':')
print(homedir)
print(sh)

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name)
print(year)

items = [1, 2, 3, 4, 5, 10, 20]
head, *tail = items
print(tail)
first, *middle, tail1, tail2 = tail
print(middle)

# COME BACK FOR THIS
items = [10, 20, 30]
def sum(items):
    head, *tail = items
    print('tail: ', tail)
    print('head: ', head)
    return head + sum(tail) if tail else head

print(sum(items))