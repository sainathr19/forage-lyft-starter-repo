import unittest
from datetime import datetime


from battery.nubbin_battery import Nubbin
from battery.spindler_battery import Splinder
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class TestBattery(unittest.TestCase):
    def nubbin_battery_needs_service_true(self):
        last_date = datetime.today().date().replace(year=datetime.today().date().year-5)
        battery = Nubbin(last_date)

        self.assertTrue(battery.battery_needs_service())\


    def nubbin_battery_needs_service_false(self):
        last_date = datetime.today().date().replace(year=datetime.today().date().year-2)
        battery = Nubbin(last_date)

        self.assertFalse(battery.battery_needs_service())

    def spindler_battery_needs_service_true(self):
        last_date = datetime.today().date().replace(year=datetime.today().date().year-3)
        battery = Splinder(last_date)

        self.assertTrue(battery.battery_needs_service())

    def spindler_battery_needs_service_false(self):
        last_date = datetime.today().date().replace(year=datetime.today().date().year-1)
        battery = Splinder(last_date)

        self.assertFalse(battery.battery_needs_service())


class TestEngine(unittest.TestCase):
    def capulet_engine_service_test_true(self):
        curr_mileage = 31000
        last_service_mileage = 0
        last_service_date = datetime.today().date().replace(datetime.today().date().year-2)
        engine = CapuletEngine(
            last_service_date, curr_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def capulet_engine_service_test_false(self):
        curr_mileage = 31000
        last_service_mileage = 30000
        last_service_date = datetime.today().date().replace(datetime.today().date().year-2)
        engine = CapuletEngine(
            last_service_date, curr_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def willoughby_engine_service_test_true(self):
        curr_mileage = 61000
        last_service_mileage = 0
        last_service_date = datetime.today().date().replace(datetime.today().date().year-2)
        engine = WilloughbyEngine(
            last_service_date, curr_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def willoughby_engine_service_test_false(self):
        curr_mileage = 61000
        last_service_mileage = 60000
        last_service_date = datetime.today().date().replace(datetime.today().date().year-2)
        engine = WilloughbyEngine(
            last_service_date, curr_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

    def sternman_engine_service_test_true(self):
        last_service_date = datetime.today().date().replace(datetime.today().date().year-2)
        warning_light = True
        engine = SternmanEngine(last_service_date, warning_light)
        self.assertTrue(engine.needs_service())

    def sternman_engine_service_test_true(self):
        last_service_date = datetime.today().date().replace(datetime.today().date().year-2)
        warning_light = False
        engine = SternmanEngine(last_service_date, warning_light)
        self.assertFalse(engine.needs_service())


if __name__ == '__main__':
    unittest.main()
