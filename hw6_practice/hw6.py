import random
from abc import ABC, abstractmethod


STATES = {0: 'sprig', 1: 'flowering', 2: 'green', 3: 'red', 4: 'rotten'}


class GardenMetaClass(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Garden(metaclass=GardenMetaClass):
    def __init__(self, vegetables, fruits, pests, gardener):
        self.vegetables = vegetables
        self.fruits = fruits
        self.pests = pests
        self.gardener = gardener

    def show_the_garden(self):
        print(f'The garden has such vegetables: {[plant.name for plant in self.vegetables]}')
        print(f'Also garden has such fruits: {[plant.name for plant in self.fruits]}')
        print(f'And such pests: {self.pests.pests_type}')
        print(f'The maintainer of the garden is {self.gardener.name}')

    @staticmethod
    def action_print(action_number, action):
        print(f'==== Action {action_number} {action} ====')

    def garden_live(self):
        '''
        This function simulating garden live with random actions
        :return:
        '''
        action_number = 0
        plants_list = self.vegetables + self.fruits
        self.show_the_garden()
        self.gardener.check_states()
        self.pests.pests_status()
        # This while loop make actions until get n-key
        while True:
            answer = input(
                '\nPress Enter for next random action \nor\nPress 0-4 key for specific action \nor\nPress n to stop:')
            action_number += 1
            if answer == 'n':
                break
            if answer.isdigit() and (int(answer) in range(0, 5)):
                action = int(answer)
            else:
                action = random.randint(0, 4)  # Getting a random next action

            if action == 0:
                self.action_print(action_number, 'Handling')
                self.gardener.handling()
            if action == 1:
                self.action_print(action_number, 'Harvest')
                self.gardener.harvest()
            if action == 2:
                self.action_print(action_number, 'Poison pests')
                self.gardener.poison_pests(target=self.pests)
            if action == 3:
                self.action_print(action_number, 'Pests breeding')
                self.pests.breed_pests()
            if action == 4:
                random.shuffle(plants_list)  # Shuffle bushes and trees in list
                self.action_print(action_number, 'Pests attack')
                self.pests.eat(plants_list)

            self.gardener.check_states()
            self.pests.pests_status()


class Gardener(ABC):
    def __init__(self, name, list_of_plants):
        self.name = name
        self.list_of_plants = list_of_plants

    @abstractmethod
    def harvest(self):
        raise NotImplementedError('Your method is not implemented.')

    @abstractmethod
    def poison_pests(self, target):
        raise NotImplementedError('Your method is not implemented.')

    @abstractmethod
    def handling(self):
        raise NotImplementedError('Your method is not implemented.')

    @abstractmethod
    def check_states(self):
        raise NotImplementedError('Your method is not implemented.')


class Pests(ABC):
    def __init__(self, pests_type, quantity):
        self.pests_type = pests_type
        self._quantity = quantity

    @property
    def quantity(self):
        return self._quantity

    @abstractmethod
    def eat(self, target):
        raise NotImplementedError('Your method is not implemented.')


class Plants(ABC):
# Parent class for vegetables and fruits classes

    def __init__(self, plant_type, name):
        self._plant_type = plant_type
        self.name = name

    @abstractmethod
    def grow(self):
        raise NotImplementedError('Your method is not implemented.')

    @abstractmethod
    def is_eatable(self):
        raise NotImplementedError('Your method is not implemented.')

    @abstractmethod
    def is_ripe(self):
        raise NotImplementedError('Your method is not implemented.')

    @abstractmethod
    def is_rotten(self):
        raise NotImplementedError('Your method is not implemented.')

    @abstractmethod
    def _change_state(self):
        raise NotImplementedError('Your method is not implemented.')

    @abstractmethod
    def print_state(self):
        raise NotImplementedError('Your method is not implemented.')


class Tomato(Plants):
    def __init__(self, index, name):
        super().__init__(plant_type='vegetable', name=name)
        self.index = index
        self._state = 0

    def grow(self):
        self._change_state()

    def is_eatable(self):
        '''
        Function for determine eatable condition for pests(green or red)
        :return: Bool
        '''
        return self._state in (2, 3)

    def is_ripe(self):
        if self._state == 3:
            return True
        return False

    def is_rotten(self):
        '''
        This function determine rotten condition
        :return: Bool
        '''
        if self._state == 4:
            return True
        return False

    def _change_state(self):
        if self._state < 4:
            self._state += 1
        self.print_state()

    def print_state(self):
        return f'{self.name} vegetable {self.index} is {STATES[self._state]}'


class TomatoBush:
    def __init__(self, num, name):
        self.tomatoes = [Tomato(index, name) for index in range(num)]
        self._tomato_number = num
        self.name = name

    def pest_attack(self, pests_quantity):
        '''
        Simulating vegetables eating by pests. Removes vegetable instance from bush if vegetable has eatable condition
        :param pests_quantity: quantity of pests
        :return: quantity of hungry pests after attack
        '''
        pests = pests_quantity
        tomatoes_list = tuple(self.tomatoes)
        for tomato in tomatoes_list:
            if tomato.is_eatable():
                print(f'Pests destroyed the {tomato.print_state()}')
                self.tomatoes.remove(tomato)
                pests -= 1
            if pests == 0:
                break
        return pests

    def grow_all(self):
        '''
        Function change states of vegetable instances and simulating appearing of new vegetables on bush
        '''
        for tomato in self.tomatoes:
            tomato.grow()  # change state
        for i in range(random.randint(0, 5)):  # bush receives 0 to 5 new vegetables
            newcomer_tomato = Tomato(self._tomato_number, self.name)
            print(f'Bush {self.name} receive {newcomer_tomato.name} {newcomer_tomato.index} ')
            self.tomatoes.append(newcomer_tomato)
            self._tomato_number += 1

    def harvest(self):
        '''
        Function remove all ripe and rotten instances from bush
        :return:
        '''
        temp_list = []
        for tomato in self.tomatoes:
            if tomato.is_ripe():
                print(f'{tomato.name} {tomato.index} have been harvested')
                continue
            if tomato.is_rotten():
                print(f'{tomato.name} {tomato.index} is rotten and has been removed')
                continue
            temp_list.append(tomato)  # add to instances list if vegetable has state less then red
        self.tomatoes = temp_list

    def show_status(self):
        print(f'\nThe {self.name} bush has:')
        for tomato in self.tomatoes:
            print(f'{tomato.print_state()}')


class Apple(Plants):
    def __init__(self, index, name):
        super().__init__(plant_type='fruit', name=name)
        self.index = index
        self._state = 0

    def grow(self):
        self._change_state()

    def is_eatable(self):
        '''
        Function for determine eatable condition for pests(green or red)
        :return: Bool
        '''
        return self._state in (2, 3)

    def is_ripe(self):
        if self._state == 3:
            return True
        return False

    def is_rotten(self):
        '''
        This function determine rotten condition
        :return: Bool
        '''
        if self._state == 4:
            return True
        return False

    def _change_state(self):
        if self._state < 4:
            self._state += 1
        self.print_state()

    def print_state(self):
        return f'{self.name} fruit {self.index} is {STATES[self._state]}'


class AppleTree:
    def __init__(self, num, name):
        self.apples = [Apple(index, name) for index in range(num)]
        self._apple_number = num
        self.name = name

    def pest_attack(self, pests_quantity):
        '''
        Simulating fruits eating by pests. Removes fruits instance from tree if vegetable has eatable condition
        :param pests_quantity: quantity of pests
        :return: quantity of hungry pests after attack
        '''
        pests = pests_quantity
        apples_list = tuple(self.apples)
        for apple in apples_list:
            if apple.is_eatable():
                print(f'Pests destroyed the {apple.print_state()}')
                self.apples.remove(apple)
                pests -= 1
            if pests == 0:
                break
        return pests

    def grow_all(self):
        '''
        Function change states of vegetable instances and simulating appearing of new fruits on tree
        :return:
        '''
        for apple in self.apples:
            apple.grow()
        for i in range(random.randint(0, 2)):  # tree receives 0 to 2 new fruits
            newcomer_apple = Apple(self._apple_number, self.name)
            print(f'Tree {self.name} receive {newcomer_apple.name} {newcomer_apple.index} ')
            self.apples.append(Apple(self._apple_number, self.name))
            self._apple_number += 1

    def harvest(self):
        temp_list = []
        for apple in self.apples:
            if apple.is_ripe():
                print(f'{apple.name} {apple.index} have been harvested')
                continue
            if apple.is_rotten():
                print(f'{apple.name} {apple.index} is rotten and has been removed')
                continue
            temp_list.append(apple)
        self.apples = temp_list

    def show_status(self):
        print(f'\nThe {self.name} tree has:')
        for apple in self.apples:
            print(f'{apple.print_state()}')


class StarGardener(Gardener):
    def __init__(self, name, list_of_plants):
        super().__init__(name=name, list_of_plants=list_of_plants)

    def harvest(self):
        for plant in self.list_of_plants:
            plant.harvest()

    def handling(self):
        for plant in self.list_of_plants:
            plant.grow_all()

    def poison_pests(self, target):
        '''
        Function simulating killing pests
        :param target: Pests object
        :return:
        '''
        target.kill_pests()

    def check_states(self):
        for plant in self.list_of_plants:
            plant.show_status()


class NastyPests(Pests):
    def __init__(self, pests_type, quantity):
        super().__init__(pests_type=pests_type, quantity=quantity)

    def eat(self, target):
        '''
        The function of simulating the destruction of plants by pests. One pest eats one Tomato or Apple instance
        :param target: list of TomatoBush and AppleTree objects
        :return:
        '''
        pest_team = self._quantity
        if pest_team > 0:
            for plant in target:
                pest_team = plant.pest_attack(pests_quantity=pest_team)
                if pest_team == 0:
                    break  # Break if all pests are full
        else:
            print('There are no pests in the garden')
            return
        if pest_team == self._quantity:
            print('Pests are hungry after attack')

    def breed_pests(self):
        '''
        Function simulating breeding of pests
        :return:
        '''
        newcomers = random.randint(1, 7)  # getting 0 to 7 new pests
        self._quantity += newcomers
        print(f'We have {newcomers} new pests. Total quantity of pasts in {self._quantity}')

    def kill_pests(self):
        self._quantity = 0
        print('All pests have been killed!!!!')

    def pests_status(self):
        print(f'\nGarden has {self._quantity} pests now')


apple_tree_1 = AppleTree(5, 'Pink_lady_tree')
tomato_bush_1 = TomatoBush(6, 'Red_tomato')
tomato_bush_2 = TomatoBush(7, 'Cherry_tomato')
vegetables = [tomato_bush_1, tomato_bush_2]
fruits = [apple_tree_1]
plants = vegetables + fruits
garden_pests = NastyPests('worm', 10)  # Implies that there is only one group of pests in the garden
tom = StarGardener('Tom', plants)  # Implies that there is only one gardener in the garden
garden = Garden(vegetables=vegetables, fruits=fruits, pests=garden_pests, gardener=tom)
garden.garden_live()

