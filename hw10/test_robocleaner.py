# Task1
# Напишіть тести до класу робота пилососа
# приклад тестів:
# робот стартує з критичними значеннями заряду батареї, наповненості баку сміття і води
# добавте аргумент час роботи (кількість ітерацій головного циклу), протестує чи зможе робот з певними вхідними
# даними закінчити прибирання можете придумати свої тести

import robo_cleaner
import unittest


class TestRoboCleaner(unittest.TestCase):
    def setUp(self) -> None:
        self.critical_battery_level = 0
        self.critical_dust_level = 100
        self.critical_water_level = 0
        self.steps = 1
        self.test_robot = robo_cleaner.RoboCleaner(self.critical_battery_level, self.critical_dust_level,
                                                   self.critical_water_level, self.steps)  # instance with critical values

    def test_battery_use(self):
        with self.assertRaises(robo_cleaner.CriticalBatteryProblem):
            self.test_robot.battery_use()
            
        with self.assertRaises(robo_cleaner.LowBatteryProblem):
            self.test_robot.battery_level = self.test_robot._warning_battery_level
            self.test_robot.battery_use()

    def test_wash(self):
        with self.assertRaises(robo_cleaner.EmptyWaterTankProblem):
            self.test_robot.wash()

    def test_vacuum(self):
        with self.assertRaises(robo_cleaner.DustContainerFullProblem):
            self.test_robot.vacuum()

    def test_cleaning_possibility(self):
        _steps = 2
        _dust_level = self.critical_dust_level - self.test_robot._dust_use * _steps
        _battery_level = self.critical_battery_level + self.test_robot._battery_use * _steps
        params = [
            [-1, 1, True],  # Task complete
            [0, 1, False],  # Dust container is full
            [-1, 0, False]  # Battery level is critical
        ]

        for a, b, c in params:
            with self.subTest(a=a, b=b, c=c):
                self.test_robot.steps = _steps
                self.test_robot.dust_level = _dust_level + a
                self.test_robot.battery_level = _battery_level + b
                self.assertEqual(self.test_robot.move(), c)


if __name__ == '__main__':
    unittest.main()


