import logging
from abc import ABC, abstractmethod

# Setup logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self) -> None:
        pass


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Vehicle:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        pass


class USVehicleFactory(VehicleFactory):
    def __init__(self, spec: str = "US Spec") -> None:
        self.spec = spec

    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(f"{make} ({self.spec})", model)

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(f"{make} ({self.spec})", model)


class EUVehicleFactory(VehicleFactory):
    def __init__(self, spec: str = "EU Spec") -> None:
        self.spec = spec

    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(f"{make} ({self.spec})", model)

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(f"{make} ({self.spec})", model)


class Car(Vehicle):
    def __init__(self, make: str, model: str) -> None:
        self.make = make
        self.model = model

    def start_engine(self) -> None:
        logger.info("%s %s Engine started", self.make, self.model)


class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str) -> None:
        self.make = make
        self.model = model

    def start_engine(self) -> None:
        logger.info("%s %s Engine started", self.make, self.model)


if __name__ == "__main__":
    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    challenger = us_factory.create_car("Dodge", "Challenger")
    challenger.start_engine()

    harley = us_factory.create_motorcycle("Harley-Davidson", "Street 750")
    harley.start_engine()

    bmw = eu_factory.create_car("BMW", "5 Series")
    bmw.start_engine()

    ducati = eu_factory.create_motorcycle("Ducati", "Monster")
    ducati.start_engine()
