# Task 2
# Напишіть клас робота пилососа
# в ініт приймається заряд батареї, заповненість сміттєбака і кількість води
#
# реалізуйте функцію move() - нескінченний цикл який на кожній ітерації "замерзає" на 1 сек
# окрім цього на кожній ітерації викликаються функції "wash" і "vacuum cleaner"
# (в цих функціях повинні стояти прніти "wash" і "vacuum cleaner" відповідно),
# також на кожній ітерації прінтиться "move"
# + на кожній ітерації цикла заряд батареї і кількість води зменшується на певну кількість
# (задайте в статік аргументах класу як конфіг пилососа, або в окремому конфіг файлі),
# а кількість сміття збільшується
#
# Напишіть власні ексепшини які кидаються коли заряд батареї менше ніж 20%, заряд батареї 0%, кількість води - 0, кількість сміття більша ніж певне число
# опрацюйте ваші ексепшини (наприклад якщо заряд батареї менше 20% то цикл робить ще певну кількість ітерацій і зупиняється,
# якщо вода закінчилась то пилосос тепер не миє підлогу а тільки пилососить,
# 0 відсотків заряду - пилосос кричить щоб його занесли на зарядку бо сам доїхати не може)
#
# можете придумати ще свої ексепшини і як їх опрацьовувати
import time


class BatteryProblem(Exception):
    def __init__(self):
        pass


class CriticalBatteryProblem(BatteryProblem):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f'CRITICAL: Battery level is critical'


class LowBatteryProblem(BatteryProblem):
    def __init__(self, warning_level):
        super().__init__()
        self.level = warning_level

    def __str__(self):
        return f'WARNING: Battery level less then {self.level}'


class EmptyWaterTankProblem(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return f'WARNING: Water tank is empty'


class DustContainerFullProblem(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return f'CRITICAL: Dust container is full'


class Cleaner:
    _battery_use = 1
    _dust_use = 5
    _water_use = 10

    def __init__(self, battery_level, dust_bucket_level, water_tank_level):
        self.battery_level = battery_level
        self.dust_level = dust_bucket_level
        self.water_level = water_tank_level

    def __str__(self):
        return f'battery level: {self.battery_level}, dust level: {self.dust_level}, water level: {self.water_level}'


class RoboCleaner(Cleaner):
    _warning_battery_level = 20

    def __init__(self, battery_level, dust_bucket_level, water_tank_level):
        super().__init__(battery_level, dust_bucket_level, water_tank_level)

    def battery_use(self):
        self.battery_level = 0 if self.battery_level <= self._battery_use else self.battery_level - self._battery_use
        if self.battery_level == 0:
            raise CriticalBatteryProblem()
        if self.battery_level < self._warning_battery_level:
            raise LowBatteryProblem(warning_level=self._warning_battery_level)

    def wash(self):
        self.water_level = 0 if self.water_level <= self._water_use else self.water_level - self._water_use
        if self.water_level == 0:
            raise EmptyWaterTankProblem()
        print('wash cleaning')

    def vacuum(self):
        self.dust_level = 100 if self.dust_level + self._dust_use >= 100 else self.dust_level + self._dust_use
        if self.dust_level == 100:
            raise DustContainerFullProblem()
        print('vacuum cleaning')

    def move(self):
        while True:
            print(f'\n{self}')
            try:
                self.battery_use()
            except BatteryProblem as err:
                print(err)
                error_type = err.__class__.__name__
                if error_type == 'CriticalBatteryProblem':
                    print('Сleaning stopped')
                    break
            try:
                self.wash()
            except EmptyWaterTankProblem as err:
                print(err)
            try:
                self.vacuum()
            except DustContainerFullProblem as err:
                print(err)
                print('Сleaning stopped')
                break

            time.sleep(1)


print('\n Cleaning 1')
robo_cleaner = RoboCleaner(battery_level=25, dust_bucket_level=0, water_tank_level=100)
robo_cleaner.move()
print('\n Cleaning 2')
robo_cleaner1 = RoboCleaner(battery_level=15, dust_bucket_level=0, water_tank_level=100)
robo_cleaner1.move()

