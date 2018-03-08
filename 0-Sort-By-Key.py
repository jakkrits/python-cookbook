from operator import attrgetter

li = [-6, -10, -19, 0, 2, 38, 199]
sorted_list = sorted(li, key=abs)
print(sorted_list)


class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({}, {}, ${}'.format(self.name, self.age, self.salary)


e1 = Employee('Carl', 49, 8000)
e2 = Employee('Jakk', 39, 2999)
e3 = Employee('Fin', 29, 9289)
employees = [e1, e2, e3]


# sort by name
def employee_name(emp):
    return emp.name


print(sorted(employees, key=employee_name))


# sort by age
def employee_age(emp):
    print('sorting employees by age')
    return emp.age


print(sorted(employees, key=employee_age, reverse=True))


# or use lambda in key
print(sorted(employees, key=lambda employee: employee.salary))


# or use attrgetter
print(sorted(employees, key=attrgetter('salary'), reverse=True))

