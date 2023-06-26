from abc import ABC, abstractmethod
from datetime import datetime


class Tire(ABC):
    def __init__(self, tire_array):
        self.tire_array = tire_array

    @abstractmethod
    def tire_needs_service(self):
        return self.tire_needs_service()
