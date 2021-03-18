from __future__ import annotations
from typing import Dict, List, Any
from abc import ABC, abstractmethod
import uuid
import random


class Animal(ABC):
    _increase_power = 0.5
    _decrease_power = -0.3

    def __init__(self, power: int, speed: int):
        self.id = None
        self.max_power = power
        self.min_power = 1
        self.current_power = power
        self.speed = speed

    @abstractmethod
    def eat(self, forest: Forest):
        raise NotImplementedError('Method not implement!')

    def _power_regeneration(self, value_percent: float):
        self.current_power += round(value_percent * self.current_power)
        if self.current_power > self.max_power:
            self.current_power = self.max_power
        if self.current_power < self.min_power:
            self.current_power = 0


class Predator(Animal):
    def __init__(self, power: int, speed: int):
        super().__init__(power, speed)

    def eat(self, forest: Forest):
        prey = forest.animals.get(str(random.choice(list(forest.animals.keys()))))  # Choosing prey animal
        while prey.current_power == 0:  # This animal already dead
            prey = forest.animals.get(str(random.choice(list(forest.animals.keys()))))  # Rechoosing prey animal

        if self.id == prey.id:
            self._power_regeneration(self._decrease_power / 2 )
            print(f'Predator {self.id} left without a dinner and loses strength. Its strength is {self.current_power} now')
        else:
            print(
                f'Predator\t\t{self.id} with speed {self.speed} strength {self.current_power} try to catch up prey\n{prey.__class__.__name__}\t\t{prey.id} with speed {prey.speed} strength {prey.current_power}')
            if (self.speed > prey.speed) and (self.current_power > prey.current_power):
                self._power_regeneration(self._increase_power)
                print(f'\tPredator {self.id} kill {prey.__class__.__name__} {prey.id} and increase strength to {self.current_power}')
                prey.current_power = 0
            else:
                self._power_regeneration(self._decrease_power)
                print(f'\tPredator {self.id} failed attack and loses strength. Its strength is {self.current_power} now')
                prey._power_regeneration(self._decrease_power)
                print(f'\t{prey.__class__.__name__} {prey.id} loses strength. Its strength is {prey.current_power} now')


class Herbivorous(Animal):
    def __init__(self, power: int, speed: int):
        super().__init__(power, speed)

    def eat(self, forest: Forest):
        self._power_regeneration(self._increase_power)
        print(f'Herbivorous {self.id} has breakfast. It strength is {self.current_power} now')


AnyAnimal = [Herbivorous, Predator]


class Forest:
    def __init__(self, animal_quantity):
        self.animals: Dict[str, AnyAnimal: Any] = dict()
        self.animal_quantity = animal_quantity
        self.__animal_item = self.__animal_value_gen()  # Generator obj

    def add_animal(self, animal: AnyAnimal):
        __uid = uuid.uuid4()
        animal.id = __uid
        self.animals[str(__uid)] = animal

    def __animal_value_gen(self):  # Generate values from animals dict
        while self.animal_quantity > 0:
            yield list(self.animals.values())[len(self.animals) - self.animal_quantity] # First index 0, last index len

    def __iter__(self):
        return self

    def __next__(self):
        if self.animal_quantity > 0:
            obj = next(self.__animal_item)  # Next value form animals dict
            self.animal_quantity -= 1
            return obj
        else:
            raise StopIteration

    def remove_animal(self, dead_animals: List):
        for animal in dead_animals:
            self.animals.pop(str(animal.id))  # Delete item from animals dict

    def any_predator_left(self):
        for item in self.animals.values():
            if isinstance(item, Predator):
                return True
        return False

    def forest_condition(self):
        self.dead_animal_check()  # Deleting dead animals
        for item in self.animals:  # Printing actual animals
            __animal = self.animals.get(item)
            print(
                f'{__animal.__class__.__name__}\t\t{__animal.id} has speed {__animal.speed} and strength {__animal.current_power}')

        self.set_animals_quantity()  # Setting new quantity of animals

    def dead_animal_check(self):
        __dead_animals = []  # list of animals with power = 0
        for item in self.animals:
            __animal = self.animals.get(item)
            if __animal.current_power <= 1:
                print(f'{__animal.__class__.__name__}\t\t{__animal.id} died')
                __dead_animals.append(__animal)
                continue
        self.remove_animal(__dead_animals)

    def set_animals_quantity(self):
        self.animal_quantity = len(self.animals)


def animal_generator(quantity_limit: int):
    item = 0
    while item < quantity_limit:
        item += 1
        yield random.choice(AnyAnimal)(power=random.randint(25, 100), speed=random.randint(25, 100))


if __name__ == "__main__":
    step_number = 0  # Information step counter
    animal_quantity = 10
    # Animals quantity in the forest

    nature = animal_generator(animal_quantity)  # Animal instance generator

    forest = Forest(animal_quantity)  # Creation forest instance
    print('Forest inhabitants:')
    for i in range(animal_quantity):
        animal = next(nature)
        forest.add_animal(animal)

    while True:
        print(f'==== Step #{step_number} ====\n')
        step_number += 1
        forest.forest_condition()  # Printing forest state
        if not forest.any_predator_left():
            print('All predators are dead')
            print('GAME OVER')
            break
        for animal in forest:
            print('')
            if animal.current_power > 1:
                animal.eat(forest=forest)
            else:
                print(f'{animal.__class__.__name__} {animal.id} already dead')
        input('Press Enter')


