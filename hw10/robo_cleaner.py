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

    def __init__(self, battery_level, dust_bucket_level, water_tank_level, work_steps):
        super().__init__(battery_level, dust_bucket_level, water_tank_level)
        self.steps = work_steps

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
        while self.steps > 0:
            print(f'\nStep to end {self.steps}')
            print(f'\n{self}')
            try:
                self.battery_use()
            except BatteryProblem as err:
                print(err)
                error_type = err.__class__.__name__
                if error_type == 'CriticalBatteryProblem':
                    print(f'\n{self}')
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
                print(f'\n{self}')
                print('Сleaning stopped')
                break

            self.steps -= 1
            time.sleep(1)
        if self.steps == 0:
            print(f'\n{self}')
            print('Task complete')
            return True
        else:
            return False


if __name__ == '__main__':
    print('\n Cleaning 1')
    robo_cleaner = RoboCleaner(battery_level=2, dust_bucket_level=94, water_tank_level=100, work_steps=1)
    robo_cleaner.move()

