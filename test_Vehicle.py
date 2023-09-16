import unittest

from Vehicle import *


class TestVehicle(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car('Lada', 'vesta', 2023)
        self.motorcycle = Motorcycle('Suzuki', 'sky line', 2012)

    def test_car_is_instance_of_vehicle(self):
        self.assertTrue(isinstance(self.car, Vehicle))  # isinstance () — это встроенная функция, которая возвращает True, если объект является экземпляром указанного класса или подкласса этого класса, и False в противном случае.

    def test_four_wheel_car(self):
        self.assertEqual(self.car.num_wheels, 4)  # assertEqual для проверки равенства двух значений

    def test_two_wheel_motorcycle(self):
        self.assertEqual(self.motorcycle.num_wheels, 2)

    def test_car_speed(self):
        self.car.test_drive()
        self.assertEqual(self.car.speed, 60)

    def test_motorcycle_speed(self):
        self.motorcycle.test_drive()
        self.assertEqual(self.motorcycle.speed, 75)

    def test_car_park_mode_after_test_drive(self):
        self.car.test_drive()
        self.car.park()
        self.assertEqual(self.car.speed, 0)

    def test_motorcycle_park_mode_after_test_drive(self):
        self.motorcycle.test_drive()
        self.motorcycle.park()
        self.assertEqual(self.motorcycle.speed, 0)


if __name__ == '__main__':
    unittest.main(verbosity=2) # verbosity=2 подробный вывод результата теста, кровни от 0-2