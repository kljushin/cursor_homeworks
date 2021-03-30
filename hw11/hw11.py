# # 1. double_result
# # This decorator function should return the result of another function multiplied by two
# def double_result(func):
#     # return function result multiplied by two
#     pass
#
#
# def add(a, b):
#     return a + b
#
#
# add(5, 5)  # 10
#
#
# @double_result
# def add(a, b):
#     return a + b
#
#
# add(5, 5)  # 20

def double_result(func):
    def wrapper():
        return func() * 2
    return wrapper


@double_result
def sixty_seven():
    return 67


result = sixty_seven()
print('Task1')
print(f'Result is {result}')

# Output:
# Task1
# Result is 134


# # 2. only_odd_parameters
# # This decorator function should only allow a function to have odd numbers as parameters,
# # otherwise return the string "Please use only odd numbers!"
#
# def only_odd_parameters(func):
#     # if args passed to func are not odd - return "Please use only odd numbers!"
#     pass
#
#
# @only_odd_parameters
# def add(a, b):
#     return a + b
#
#
# add(5, 5)  # 10
# add(4, 4)  # "Please use only odd numbers!"
#
#
# @only_odd_parameters
# def multiply(a, b, c, d, e):
#     return a * b * c * d * e


def only_odd_parameters(func):
    def wrapper(*args):
        if [x for x in args if x % 2 == 0]:
            return "Please use only odd numbers!"
        else:
            return func(*args)
    return wrapper


@only_odd_parameters
def add(a, b):
    return a + b


@only_odd_parameters
def multiply(a, b, c, d, e):
    return a * b * c * d * e


print('Task2')
print(add(5, 7))
print(add(2, 4))
print(multiply(1, 2, 3, 4, 5))
print(multiply(1, 3, 5, 7, 11))

# Output:
# Task2
# 12
# Please use only odd numbers!
# Please use only odd numbers!
# 1155

# # 3.* logged
# # Write a decorator which wraps functions to log function arguments and the return value on each call.
# # Provide support for both positional and named arguments (your wrapper function should take both *args
# # and **kwargs and print them both):
#
# def logged(func):
#     # log function arguments and its return value
#     pass
#
#
# @logged
# def func(*args):
#     return 3 + len(args)
#
#
# func(4, 4, 4)
#
#
# # you called func(4, 4, 4)
# # it returned 6

from functools import wraps


def logged(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_list = [repr(item) for item in args]
        kwargs_list = [f'{key}={val}' for key, val in kwargs.items()]
        signature = ', '.join(args_list + kwargs_list)
        print(f'Called {func.__name__}({signature})')
        result = func(*args, **kwargs)
        print(f'it returned {result}')
        return result
    return wrapper


@logged
def func(*args, **kwargs):
    return 100 + len(args) + len(kwargs)


print('Task3')
print(func(4, 2, 3))
print(func({'four': 4, 'two': 2}, {'qwe': 'qwe'}))
print(func(4, 2, 3, {'four': 4, 'two': 2}, {'qwe': 'qwe'}))

# Output:
# Task3
# Called func(4, 2, 3)
# it returned 103
# 103
# Called func({'four': 4, 'two': 2}, {'qwe': 'qwe'})
# it returned 102
# 102
# Called func(4, 2, 3, {'four': 4, 'two': 2}, {'qwe': 'qwe'})
# it returned 105
# 105

# # 4. type_check
# # you should be able to pass 1 argument to decorator - type.
# # decorator should check if the input to the function is correct based on type.
# # If it is wrong, it should print(f"Wrong Type: {type}"), otherwise function should be executed.
#
# def type_check(correct_type):
#     # put code here
#     pass
#
#
# @type_check(int)
# def times2(num):
#     return num * 2
#
#
# print(times2(2))
# times2('Not A Number')  # "Wrong Type: string" should be printed, since non-int passed to decorated function
#
#
# @type_check(str)
# def first_letter(word):
#     return word[0]
#
#
# print(first_letter('Hello World'))
# first_letter(['Not', 'A', 'String'])  # "Wrong Type: list" should be printed, since non-str passed to decorated
# function


def type_check(correct_type):
    def type_check_decorator(func):
        def wrapper(arg):
            if isinstance(arg, correct_type):
                return func(arg)
            else:
                return f'Wrong type: {type(arg).__name__}'
        return wrapper
    return type_check_decorator


@type_check(int)
def times2(num):
    return num * 2


@type_check(str)
def first_letter(word):
    return word[0]


print('Task4')
print(times2(2))
print(times2('Not A Number'))

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))

# Output:
# Task4
# 4
# Wrong type: str
# H
# Wrong type: list
