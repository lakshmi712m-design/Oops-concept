from abc import ABC ,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
class car(Vehicle):
    def start_engine(self):
        print("the car engine started")
class bike(Vehicle):
    def start_engine(self):
        print("the bike engine started")
class bus(Vehicle):
    def start_engine(self):
        print("the bus engine started") 

car1=car()
car1.start_engine()