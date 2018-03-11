def outer_function(arg):

    def inner_function():
        print(arg)

    return inner_function


hi_func = outer_function('Hi')
bye_func = outer_function('Bye')

hi_func()
hi_func()
bye_func()
bye_func()


print('*+-!' * 10)


def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function


def display():
    print('display function ran')


decorated_display = decorator_function(display)

decorated_display()

# decorator allows us to modify functionality by leaving original function alone
# by adding stuff to wrapper function
# like so:

print('-0' * 30)


def mod_decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('Wrapper executed before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function


def mod_display():
    print('display function ran')


mod_decorated_display = mod_decorator_function(mod_display)

mod_decorated_display()

print('+ - !' * 10)
# you can use @decorator to add functionalities to you original function


@mod_decorator_function
def func_needs_added_functionalities():
    print('I got added functionalities!')


func_needs_added_functionalities()

print('--' * 20)


@mod_decorator_function
def display_info(name, age):
    print('display {}: age {}'.format(name, age))


display_info('jakk', 29)

print('-- ' * 30)

"""
CLASS DECORATOR
"""


class DecoratorClass(object):
    def __init__(self, original_function):
        self.original_function = original_function
    # when init instance of this class, set it to that function

    def __call__(self, *args, **kwargs):
        print('call method executed this before {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)
    # invoke it


@DecoratorClass
def display_function():
    print('display function just ran!')


@DecoratorClass
def display_function_with_argument(name, age):
    print(f'{name.upper()} age = {age}')


display_function()
display_function_with_argument('จักกิด', 22)


# STACK DECORATORS
# lower runs first
# from functools import wraps
# DECORATE wraps(original_function) to your wrapper_function()