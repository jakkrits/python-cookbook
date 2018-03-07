"""
We want to sort data pulled from database
"""
from operator import itemgetter

rows = [
    {'first_name': 'Brian', 'last_name': 'Jones', 'uid': 1003},
    {'first_name': 'David', 'last_name': 'Beazley', 'uid': 1002},
    {'first_name': 'John', 'last_name': 'Cleese', 'uid': 1001},
    {'first_name': 'Big', 'last_name': 'Jones', 'uid': 1004}
]

rows_by_firstname = sorted(rows, key=itemgetter('first_name'))
rows_by_lastname = sorted(rows, key=itemgetter('last_name'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))

# it can accept multiple keys
rows_by_first_and_last = sorted(rows, key=itemgetter('first_name', 'last_name'))

print(rows_by_uid)
print('*'*80)
print(rows_by_first_and_last)

# can combine with min() max()
min(rows, key=itemgetter('first_name'))
max(rows, key=itemgetter('uid'))

# itemgetter() is equivalent to lambda
rows_by_firstname_lambda = sorted(rows, key=lambda r: (r['first_name']))
rows_by_lastname_lambda = sorted(rows, key=lambda r: (r['first_name'], r['last_name']))
print('*'*60)

print(rows_by_firstname_lambda)
