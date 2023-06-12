from typing import Any


class Car:
    def __init__(self, make, model, price) -> None:
        super().__init__()
        self.make = make
        self.model = model
        self.price = price
        self._discount = 0.25

    #работает при каждом вызове переменной 
    def __getattribute__(self, __name: str) -> Any:
        if __name == "price":
            p = super().__getattribute__("price")
            d = super().__getattribute__("_discount")
            return p - (p * d)
        return super().__getattribute__(__name)
    
    #вызывается если нет атрибута 
    def __getattr__(self, __name: str) -> str:
        return __name + " not implemented"

    #установка атрибутов
    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name == "price":
            if type(__value) is not float:
                raise ValueError("price is not float")
        return super().__setattr__(__name, __value)
    
    #вызываем объект как функцию 
    def __call__(self, __make, __model, __price) -> Any:
        self.make = __make
        self.model = __model
        self.price = __price
        self._discount = 0.25
    
    #возвращет только стр
    def __str__(self) -> str:
        return f"{self.make} {self.model} cost {self.price}"
    
    #возвращает любой тип данных
    def __repr__(self):
        return f"{self.make} {self.model} cost11 {self.price}"
    
    #сравнение экземпляров класса
    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Car):
            raise ValueError("cant compare")
        return (self.make == __value.make and
                self.model == __value.model)
    
    #>=
    def __ge__(self, __value: object) -> bool:
        if not isinstance(__value, Car):
            raise ValueError("cant compare")
        return (self.price >= __value.price)
    
    def __lt__(self, __value: object) -> bool:
        if not isinstance(__value, Car):
            raise ValueError("cant compare")
        return (self.price < __value.price)

car1 = Car("toyota", "camry", 7000.0)
car2 = Car("opel", "astra", 5000.0)
car3 = Car("mersedes", "gt black", 19000.0)

'''
#print(str(car2))
#print(repr(car1))
#print(car2 == car3)

#print(car2 >= car1)
#print(car2 < car1)

cars = [car1, car2, car3]
cars.sort(reverse=True)
print([car.price for car in cars])
'''

# car1.price = 7500.0
# print(car1)

car1("WV", "passat", 6000.00)

print(car1.__dict__)
