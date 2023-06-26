from tire import Tire
from datetime import datetime


class Carrigan(Tire):
    def __init__(self, tyre_value):
        super().__init__(tyre_value)
        self.tyre_value = tyre_value

    def tire_needs_service(self):
        for i in self.tyre_value:
            if (i > 0.9):
                return True
        return False
