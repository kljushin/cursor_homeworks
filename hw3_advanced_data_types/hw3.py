# 1. Define the id of next variables:

int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}
print('1.')
print('int_a id is ', id(int_a))
print('str_b id is ', id(str_b))
print('set_c id is ', id(set_c))
print('lst_d id is ', id(lst_d))
print('dict_e id is ', id(dict_e))

# Output:
# 1.
# int_a id is  9786592
# str_b id is  139995246844080
# set_c id is  139995247897952
# lst_d id is  139995247652672
# dict_e id is  139995248128384

# 2. Append 4 and 5 to the lst_d and define the id one more time.

lst_d.append(4)
lst_d.append(5)
print('2.')
print('lst_d:', lst_d)
print('lst_d id is ', id(lst_d))

# Output:
# 2.
# lst_d: [1, 2, 3, 4, 5]
# lst_d id is  139995247652672

# 3. Define the type of each object from step 1.

print('3.')
print('int_a type is ', type(int_a))
print('str_b type is ', type(str_b))
print('set_c type is ', type(set_c))
print('lst_d type is ', type(lst_d))
print('dict_e type is ', type(dict_e))

# Output:
# 3.
# int_a type is  <class 'int'>
# str_b type is  <class 'str'>
# set_c type is  <class 'set'>
# lst_d type is  <class 'list'>
# dict_e type is  <class 'dict'>

# 4*. Check the type of the objects by using isinstance.

print('4.')
print('Is int_a has type int? ', isinstance(int_a, int))
print('Is str_b has type str? ', isinstance(str_b, str))
print('Is set_c has type set? ', isinstance(set_c, set))
print('Is lst_d has type lst? ', isinstance(lst_d, list))
print('Is dict_e has type dict? ', isinstance(dict_e, dict))

# Output:
# 4.
# Is int_a has type int?  True
# Is str_b has type str?  True
# Is set_c has type set?  True
# Is lst_d has type lst?  True
# Is dict_e has type dict?  True

# String formatting:
# Replace the placeholders with a value:
# "Anna has ___ apples and ___ peaches."

# 5. With .format and curly braces {}

apples = 100
peaches = 500

print('5.')
print('Anna has {} apples and {} peaches.'.format(apples, peaches))

# Output:
# 5.
# Anna has 100 apples and 500 peaches.

# 6. By passing index numbers into the curly braces.

print('6.')
print('Anna has {1} apples and {0} peaches.'.format(peaches, apples))

# Output:
# 6.
# Anna has 100 apples and 500 peaches.

# 7. By using keyword arguments into the curly braces.

print('7.')
print('Anna has {apples_amount} apples and {peaches_amount} peaches.'.format(apples_amount=1, peaches_amount=-3))

# Output:
# 7.
# Anna has 1 apples and -3 peaches.

# 8*. With indicators of field size (5 chars for the first and 3 for the second)

print('8.')
print('Anna has {0:5} apples and {1:3} peaches.'.format('five', 3))

# Output:
# 8.
# Anna has five  apples and   3 peaches.

# 9. With f-strings and variables

apples = 10
peaches = 'two'
fruits = apples, peaches

print('9.')
print(f'Anna has {fruits[0]} apples and {fruits[1]} peaches.')

# Output:
# 9.
# Anna has 10 apples and two peaches.


# 10. With % operator

print('10.')
print('Anna has %s apples and %d peaches.' % ('007', 0x10))

# Output:
# 10.
# Anna has 007 apples and 16 peaches.

# 11*. With variable substitutions by name (hint: by using dict)

fruits_dict = {'cucumbers': 3, 'peaches': 2, 'apples': None}

print('11.')
print('Anna has %(apples)s apples and %(peaches)d peaches.' % fruits_dict)

# Output:
# 11.
# Anna has None apples and 2 peaches.

# Comprehensions:
# (1)
# lst = []
# for num in range(10):
#     if num % 2 == 1:
#         lst.append(num ** 2)
#     else:
#         lst.append(num ** 4)
# print(lst)
#
# (2)
# list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]

# 12. Convert (1) to list comprehension

lst = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]

print('12.')
print(lst)

# Output:
# 12.
# [0, 1, 16, 9, 256, 25, 1296, 49, 4096, 81]

# 13. Convert (2) to regular for with if-else
# list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]

list_comprehension_test = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]  # test
list_comprehension = []

for num in range(10):
    if num % 2 == 0:
        list_comprehension.append(num // 2)
    else:
        list_comprehension.append(num * 10)

print('13.')
print('test:', list_comprehension_test)
print('my:  ', list_comprehension)

# Output:
# 13.
# test: [0, 10, 1, 30, 2, 50, 3, 70, 4, 90]
# my:   [0, 10, 1, 30, 2, 50, 3, 70, 4, 90]

# 14. Convert (3) to dict comprehension.
# (3)
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
# print(d)

print('14.')
d_test = {}
for num in range(1, 11):
    if num % 2 == 1:
        d_test[num] = num ** 2
print('test:', d_test)  # test

d = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}

print('my  :', d)

# Output:
# 14.
# test: {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
# my  : {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# 15*. Convert (4) to dict comprehension.
# (4)
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
#     else:
#         d[num] = num // 0.5
# print(d)

d = {}  # test
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
    else:
        d[num] = num // 0.5
print('15.')
print('test:', d)

d_my = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}

print('my  :', d_my)

# Output:
# 15.
# test: {1: 1, 2: 4.0, 3: 9, 4: 8.0, 5: 25, 6: 12.0, 7: 49, 8: 16.0, 9: 81, 10: 20.0}
# my  : {1: 1, 2: 4.0, 3: 9, 4: 8.0, 5: 25, 6: 12.0, 7: 49, 8: 16.0, 9: 81, 10: 20.0}

# 16. Convert (5) to regular for with if.
# (5)
# dict_comprehension = {x: x ** 3 for x in range(10) if x ** 3 % 4 == 0}

dict_comprehension = {x: x ** 3 for x in range(10) if x ** 3 % 4 == 0}  # test

print('16.')
print('test:', dict_comprehension)

my_dict_comprehension = {}

for x in range(10):
    if x ** 3 % 4 == 0:
        my_dict_comprehension[x] = x ** 3

print('my:  ', my_dict_comprehension)

# Output:
# 16.
# test: {0: 0, 2: 8, 4: 64, 6: 216, 8: 512}
# my:   {0: 0, 2: 8, 4: 64, 6: 216, 8: 512}

# 17*. Convert (6) to regular for with if-else.
# (6)
# dict_comprehension = {x: x ** 3 if x ** 3 % 4 == 0 else x for x in range(10)}

dict_comprehension = {x: x ** 3 if x ** 3 % 4 == 0 else x for x in range(10)}  # test

print('17.')
print('test:', dict_comprehension)

my_dict_comprehension = {}

for x in range(10):
    if x ** 3 % 4 == 0:
        my_dict_comprehension[x] = x ** 3
    else:
        my_dict_comprehension[x] = x

print('my  :', my_dict_comprehension)


# Output
# 17.
# test: {0: 0, 1: 1, 2: 8, 3: 3, 4: 64, 5: 5, 6: 216, 7: 7, 8: 512, 9: 9}
# my  : {0: 0, 1: 1, 2: 8, 3: 3, 4: 64, 5: 5, 6: 216, 7: 7, 8: 512, 9: 9}

# 18. Convert (7) to lambda function
# (7)
# def foo(x, y):
#     if x < y:
#         return x
#     else:
#         return y


def foo(x, y):
    if x < y:
        return x
    else:
        return y


print('18.')
print('test:', foo(0, 1))

my_foo = lambda x, y: x if x < y else y  # lambda x, y: min(x,y)
print('my  :', my_foo(0, 1))

print('test:', foo('asd', 'qwe'))
print('my  :', my_foo('asd', 'qwe'))

print('test:', foo(1, 1))
print('my  :', my_foo(1, 1))

# Output
# 18.
# test: 0
# my  : 0
# test: asd
# my  : asd
# test: 1
# my  : 1

# 19*. Convert (8) to regular function
# (8)
# foo = lambda x, y, z: z if y < x and x > z else y

foo = lambda x, y, z: z if y < x and x > z else y  # test


def my_foo(x, y, z):
    return z if y < x and x > z else y


print('19.')
print('test:', foo(1, 2, 3))
print('my  :', my_foo(1, 2, 3))
print('test:', foo('d', 'b', 'a'))
print('my  :', my_foo('d', 'b', 'a'))

# Output:
# 19.
# test: 2
# my  : 2
# test: a
# my  : a

# 20. Sort lst_to_sort from min to max

lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]

print('20.')
print(sorted(lst_to_sort))

# Output:
# 20.
# [1, 5, 13, 15, 18, 24, 33, 55]

# 21. Sort lst_to_sort from max to min

print('21.')
print(sorted(lst_to_sort, reverse=True))

# Output:
# 21.
# [55, 33, 24, 18, 15, 13, 5, 1]

# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2

lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]

print('22.')
print('lst_to_sort:', lst_to_sort)
print('updated:', list(map(lambda x: x * 2, lst_to_sort)))

# Output:
# 22.
# lst_to_sort: [5, 18, 1, 24, 33, 15, 13, 55]
# updated: [10, 36, 2, 48, 66, 30, 26, 110]

# 23*. Raise each list number to the corresponding number on another list:
# list_A = [2, 3, 4]
# list_B = [5, 6, 7]

list_A = [2, 3, 4]
list_B = [5, 6, 7]

print('23.')
print('list_A:', list_A)
print('list_B:', list_B)

raised_list_A = list(map(lambda a, b: a ** b, list_A, list_B))
print('raised list_A:', raised_list_A)

# Output:
# 23.
# list_A: [2, 3, 4]
# list_B: [5, 6, 7]
# raised list_A: [32, 729, 16384]

# 24. Use reduce and lambda to compute the numbers of a lst_to_sort.

from functools import reduce

lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]

print('24.')
print('Computation result: ', reduce(lambda x, y: x + y, lst_to_sort))

# Output:
# 24.
# Computation result:  164

# 25. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.

lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]

print('25.')
print('lst_to_sort', lst_to_sort)
print('filtered list:',list(filter(lambda elem: elem % 2 == 1, lst_to_sort)))

# Output:
# 25.
# lst_to_sort [5, 18, 1, 24, 33, 15, 13, 55]
# filtered list: [5, 1, 33, 15, 13, 55]

# 26. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.

b = range(-10, 10)
print('26.')
print('Filter negative numbers:', list(filter(lambda x: x < 0, b)))

# Output:
# 26.
# Filter negative numbers: [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]

# 27*. Using the filter function, find the values that are common to the two lists:
# list_1 = [1,2,3,5,7,9]
# list_2 = [2,3,5,6,7,8]

list_1 = [1, 2, 3, 5, 7, 9]
list_2 = [2, 3, 5, 6, 7, 8]

print('27.')
print('list_1', list_1)
print('list_2', list_2)

lst = list_2

print('Common items:', list(filter(lambda item: item in lst, list_1)))

# Output
# 27.
# list_1 [1, 2, 3, 5, 7, 9]
# list_2 [2, 3, 5, 6, 7, 8]
# Common items: [2, 3, 5, 7]

