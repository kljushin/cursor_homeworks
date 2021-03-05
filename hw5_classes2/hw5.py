# 1.
# class Laptop:
#     """
#     Make the class with composition.
#     """
# class Battery:
#     """
#     Make the class with composition.
#     """

class Laptop:
    def __init__(self, laptop_name, laptop_model, battery_model, battery_type, battery_capacity):
        self.laptop_name = laptop_name
        self.laptop_model = laptop_model
        # self.battery_model = battery_model
        # self.battery_type = battery_type
        # self.battery_capacity = battery_capacity
        # Composition
        self.laptop_battery = Battery(battery_model, battery_type, battery_capacity)

    def __str__(self):
        return f'{self.laptop_name} {self.laptop_model} with battery {self.laptop_battery}'


class Battery:
    def __init__(self, battery_model, battery_type, battery_capacity):
        self.battery_model = battery_model
        self.battery_type = battery_type
        self.battery_capacity = battery_capacity

    def __str__(self):
        return f'{self.battery_model} {self.battery_type} {self.battery_capacity}'


dell_laptop = Laptop('DELL', 'Inspiron G5 5500', 'UX1245', 'Li-ion', '51Wh')
print(dell_laptop)


# Output:
# DELL Inspiron G5 5500 with battery UX1245 Li-ion 51Wh


# 2.
# class Guitar:
#     """
#     Make the class with aggregation
#     """
# class GuitarString:
#     """
#     Make the class with aggregation
#     """

class Guitar:
    def __init__(self, guitar_name, *args):
        self.guitar_name = guitar_name
        self.guitar_strings = args

    def __str__(self):
        # Output guitar name and string_tone attr of GuitarString objects from guitar_strings list
        return f'{self.guitar_name} has {", ".join(list(map(lambda x: x.string_tone, self.guitar_strings)))} strings'


class GuitarString:
    def __init__(self, string_tone):
        self.string_tone = string_tone

    def __str__(self):
        return f'string {self.string_tone}'


string_G = GuitarString('G')
string_D = GuitarString('D')
string_H = GuitarString('H')
string_E = GuitarString('E')

bass = Guitar('Ibanez 4 String Bass Guitar', string_G, string_D, string_H, string_E)
print(bass)


# Output
# Ibanez 4 String Bass Guitar has G, D, H, E strings


# 3
# class Calc:
#     """
#     Make class with one method "add_nums" with 3 parameters, which returns sum of these parameters.
#     Note: this method should not take instance as first parameter.
#     """

class Calc:
    @staticmethod
    def add_nums(x, y, z):
        return x + y + z


numbers = Calc()
print(Calc.add_nums(1, 2, 10))

# Output:
# 13

# 4*.
# class Pasta:
#     """
#     Make class which takes 1 parameter on init - list of ingredients and defines instance attribute ingredients.
#     It should have 2 methods:
#     carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
#     which should create Pasta instances with predefined list of ingredients.
#     Example:
#         pasta_1 = Pasta(["tomato", "cucumber"])
#         pasta_1.ingredients will equal to ["tomato", "cucumber"]
#         pasta_2 = Pasta.bolognaise()
#         pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']
#     """


class Pasta:
    __carbonara_ingredient = ['forcemeat', 'tomatoes']
    __bolognaise_ingredient = ['bacon', 'parmesan', 'eggs']

    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def carbonara(cls):
        return Pasta(cls.__carbonara_ingredient)

    @classmethod
    def bolognaise(cls):
        return Pasta(cls.__bolognaise_ingredient)


pasta_1 = Pasta(["tomato", "cucumber"])
print(f'pasta_1 ingredients is {pasta_1.ingredients}')
pasta_2 = Pasta.bolognaise()
print(f'pasta_2 ingredients is {pasta_2.ingredients}')
pasta_3 = Pasta.carbonara()
print(f'pasta_3 ingredients is {pasta_3.ingredients}')


# Output:
# pasta_1 ingredients is ['tomato', 'cucumber']
# pasta_2 ingredients is ['bacon', 'parmesan', 'eggs']
# pasta_3 ingredients is ['forcemeat', 'tomatoes']


# 5*.
# class Concert:
#     """
#     Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
#     In case of setting visitors_count - max_visitors_num should be checked,
#     if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
#     Example:
#         Concert.max_visitor_num = 50
#         concert = Concert()
#         concert.visitors_count = 1000
#         print(concert.visitors_count)  # 50
#     """


class Concert:
    max_visitors_num = 0

    def __init__(self, visitors_count=0):
        self._visitors_count = visitors_count

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, visitors):
        if visitors > self.max_visitors_num:
            self._visitors_count = self.max_visitors_num
        else:
            self._visitors_count = visitors


concert1 = Concert()
concert2 = Concert()

Concert.max_visitors_num = 50

print('concert1.max_visitors_num:', concert1.max_visitors_num)
concert1.visitors_count = 1000
print('concert1.visitors_count: ', concert1.visitors_count)

Concert.max_visitors_num = 5000

print('concert2.max_visitors_num:', concert2.max_visitors_num)
concert2.visitors_count = 2000
print('concert2.visitors_count: ', concert2.visitors_count)

# Output:
# concert1.max_visitors_num: 50
# concert1.visitors_count:  50
# concert2.max_visitors_num: 5000
# concert2.visitors_count:  2000


# 6.
# class AddressBookDataClass:
#     """
#     Create dataclass with 7 fields - key (int), name (str), phone_number (str), address (str), email (str),
#     birthday (str), age (int)
#     """

import dataclasses


@dataclasses.dataclass()
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


address_book = AddressBookDataClass(123, 'Boris', '11-22-33', 'Kyiv', 'qwe@gmail.com', '01-01-2000', 20)
print(address_book)

# Output
# AddressBookDataClass(key=123, name='Boris', phone_number='11-22-33', address='Kyiv', email='qwe@gmail.com',
# birthday='01-01-2000', age=20)


# 7. Create the same class (6) but using NamedTuple

import collections

AddressBookDataClass1 = collections.namedtuple('AddressBookDataClass1',
                                               ['key', 'name', 'phone_number', 'address', 'email', 'birthday', 'age'])


address_book1 = AddressBookDataClass1(123, 'Boris', '11-22-33', 'Kyiv', 'qwe@gmail.com', '01-01-2000', 20)
print(address_book1)

# Output
# AddressBookDataClass1(key=123, name='Boris', phone_number='11-22-33', address='Kyiv', email='qwe@gmail.com',
# birthday='01-01-2000', age=20)


# 8.
# class AddressBook:
#     """
#     Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
#     Make its str() representation the same as for AddressBookDataClass defined above.
#     """

class AddressBook:
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self. phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return f'{__class__.__name__}(key={self.key}, name={self.name}, phone_number={self.phone_number}, ' \
               f'address={self.address}, email={self.email}, birthday={self.birthday}, age={self.age})'


address_book3 = AddressBook(123, 'Boris', '11-22-33', 'Kyiv', 'qwe@gmail.com', '01-01-2000', 20)
print(address_book3)

# Output
# AddressBook(key=123, name=Boris, phone_number=11-22-33, address=Kyiv, email=qwe@gmail.com,
# birthday=01-01-2000, age=20)


# 9.


class Person:
    """
    Change the value of the age property of the person object
    """
    name = "John"
    age = 36
    country = "USA"


person = Person()
print('person age = ', person.age)
person.age = 1000
print('person age = ', person.age)

# Output
# person age =  36
# person age =  1000


# 10.


class Student:
    """
    Add an 'email' attribute of the object student and set its value
    Assign the new attribute to 'student_email' variable and print it by using getattr
    """
    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name


student = Student(id=124, name='Boris')

student.email = 'asd@qwe.com'
student_email = getattr(student, 'email')
print('student_email is', student_email)


# Output
# student_email is asd@qwe.com


# 11*.

class Celsius:
    """
    By using @property convert the celsius to fahrenheit
    Hint: (temperature * 1.8) + 32)
    """
    # create an object
    # {obj} = ...
    #
    # print({obj}.temperature)

    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def temperature(self):
        return (self._temperature * 1.8) + 32


celsius_temperature = 2
t = Celsius(celsius_temperature)

print(f'{celsius_temperature}\u2103 is {t.temperature}\u2109')

# Output:
# 2℃ is 35.6℉
