# 1. Create a Vehicle class with max_speed and mileage instance attributes

class Vehicle:
    def __init__(self, max_speed, mileage: object):
        self.max_speed = max_speed
        self.mileage = mileage


# 2. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class and will have seating_capacity own method

class Bus(Vehicle):
    def __init__(self, max_speed, mileage, seating_capacity):
        super().__init__(max_speed, mileage)
        self.seating_capacity = seating_capacity



bus1 = Bus(500, 1, 1)
bus2 = Bus(100, 111, 0)
for item in (bus1, bus2):
    print('Object:', item)
    print(item.max_speed)
    print(item.mileage)
    print(item.seating_capacity)

# Output:
# Object: <__main__.Bus object at 0x7f472cb018b0>
# 500
# 1
# 1
# Object: <__main__.Bus object at 0x7f472cb01d60>
# 100
# 111
# 0

# 3. Determine which class a given Bus object belongs to (Check type of an object)

print('Type of bus1 object:', type(bus1))
print('Is bus1 instance of Bus?:', isinstance(bus1, Bus))
print('Is bus1 instance of Vehicle?:', isinstance(bus1, Vehicle))
print('Is class Bus inheritance class Vehicle?', issubclass(Bus, Vehicle))

# Output:
# Type of bus1 object: <class '__main__.Bus'>
# Is bus1 instance of Bus?: True
# Is bus1 instance of Vehicle?: True
# Is class Bus inheritance class Vehicle? True


# 4. Determine if School_bus is also an instance of the Vehicle class

# I haven`t class School_bus yet

# 5. Create a new class School with get_school_id and number_of_students instance attributes

class School:
    def __init__(self, number_of_students):
        self.number_of_students = number_of_students

    def get_school_id(self):
        return 'I`m get school_id method'


# 6*. Create a new class SchoolBus that will inherit all of the methods from School
# and Bus and will have its own - bus_school_color


class SchoolBus(School, Bus):
    def __init__(self, number_of_students, max_speed, mileage, seating_capacity, bus_school_color):
        School.__init__(self, number_of_students)
        Bus.__init__(self, max_speed, mileage, seating_capacity)
        self.bus_school_color = bus_school_color


school_bus = SchoolBus(123, 500, 0, 100, 'yellow')

print(f'school_bus: {school_bus.__dict__} ')
print('Is class SchoolBus inheritance class Vehicle?', issubclass(SchoolBus, Vehicle))  # Task 4

# Output:
# school_bus: {'number_of_students': 123, 'max_speed': 500, 'mileage': 0, 'seating_capacity': 100, 'bus_school_color': 'yellow'}
# Is class SchoolBus inheritance class Vehicle? True

# 7. Polymorphism: Create two classes: Bear, Wolf. Both of them should have make_sound method. Create two instances, one of Bear and one of Wolf,
# make a tuple of it and by using for call their action using the same method.


class Bear:
    def __init__(self):
        pass

    def make_sound(self):
        return "Grrrrr"


class Wolf:
    def __init__(self):
        pass

    def make_sound(self):
        return "Wooooo"


bear = Bear()
wolf = Wolf()

for animal in (bear, wolf):
    print("Make sound: ", animal.make_sound())

# Output:
# Make sound:  Grrrrr
# Make sound:  Wooooo

# Magic methods:
# 8. Create class City with name, population instance attributes, return a new instance only when population > 1500,
# otherwise return message: "Your city is too small".


class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __new__(cls, name, population):
        instance = super(City, cls).__new__(cls)
        if population > 1500:
            return instance
        else:
            return 'Your city is too small'

    def __str__(self):
        return f'{self.__class__.__name__}{self.__dict__}'


city1 = City('Kyiv', 3000000)
print(city1)
city2 = City('Chernobyl', 0)
print(city2)

# Output:
# City{'name': 'Kyiv', 'population': 3000000}
# Your city is too small

# 9. Override a printable string representation of the City class and return: The population of the city {name} is {population}

class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __new__(cls, name, population):
        instance = super(City, cls).__new__(cls)
        if population > 1500:
            return instance
        else:
            return 'Your city is too small'

    def __str__(self):
        return f'Population of {self.name} is {self.population}'


city1 = City('Kyiv', 3000000)
city2 = City('Chernobyl', 0)
print(city1)
print(city2)

# Output:
# Population of Kyiv is 3000000
# Your city is too small

# 10*. Override magic method __add__() to perform the additional action as 'multiply' (*) the value which is greater than 10. And perform this add (+) of two instances.


class Count:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        if self.number > 10:
            return self.number * other.number
        else:
            return self.number + other.number


a = Count(10)
b = Count(101)
total1 = a + b
total2 = b + a
print(f'{a.number} + {b.number} = ', total1)
print(f'{b.number} + {a.number} = ', total2)

# Output:
# 10 + 101 =  111
# 101 + 10 =  1010

# 11. The __call__ method enables Python programmers to write classes where the instances behave like functions and can be called like a function.
# Create a new class with __call__ method and define this call to return sum.


class SumClass:

    def __call__(self, *args):
        return sum(args)


total3 = SumClass()

print(total3(100, 11))
print(total3(1, 2, 3))
print(total3())

# Output:
# 111
# 6
# 0


# 12*. Making Your Objects Truthy or Falsey Using __bool__().
# Create class MyOrder with cart and customer instance attributes.
# Override the __bool__magic method considered to be truthy if the length of the cart list is non-zero.
# e.g.:
# order_1 = MyOrder(['a', 'b', 'c'], 'd')
# order_2 = MyOrder([], 'a')
# bool(order_1)
# True
# bool(order_2)
# False

class MyOrder:
    def __init__(self, cart, customer):
        self.cart = cart
        self.customer = customer

    def __bool__(self):
        return False if len(self.cart) == 0 else True


order_1 = MyOrder(['a', 'b', 'c'], 'd')
order_2 = MyOrder([], 'a')

print(f'{order_1.__dict__} {bool(order_1)}')
print(f'{order_2.__dict__} {bool(order_2)}')

# Output:
# {'cart': ['a', 'b', 'c'], 'customer': 'd'} True
# {'cart': [], 'customer': 'a'} False
