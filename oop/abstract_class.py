from abc import ABC, abstractmethod

#интерфейс

class Shipping(ABC):
    @abstractmethod
    def shipping(self, transport):
        pass

class Electrical_Appliance(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def electricity_consumption():
        pass

class Heater(Electrical_Appliance, Shipping):
    def __init__(self, heating) -> None:
        self.heating = heating

    def electricity_consumption(self) -> int:
        return 1500 * self.heating
    
    def shipping(self, transport):
        self.transport = transport
        return transport
        
class Coler():
    def __init__(self, cooling) -> None:
        self.cooling = cooling

    def electricity_consumption(self) -> int:
        return 300 * self.cooling
    
e = Coler(50)
print(e.cooling, e.electricity_consumption())
v = Heater(50)
print(v.heating, v.electricity_consumption(), v.shipping("cargo"))