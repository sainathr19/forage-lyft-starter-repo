from tire import Tire


class Octoprime(Tire):
    def __int__(self, tyre_value):
        super().__init__(tyre_value)
        self.tyre_value = tyre_value

    def tire_needs_service(self):
        return sum(self.tyre_value) > 3
