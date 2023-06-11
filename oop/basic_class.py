class Car:
    #глобальные переменные 
    PURCHASE_TYPES = ('LEASE', 'CASH')

    #статический метод
    __sales_list = None

    @staticmethod
    def get_sales_list() -> list:
        if Car.__sales_list == None:
            Car.__sales_list = []
        return Car.__sales_list

    #метод класса, а не экземпляра класса
    @classmethod
    def get_purchase_types(cls) -> tuple:
        return cls.PURCHASE_TYPES

    def __init__(self, marker, model, colour, price, purchase_type) -> None:
        self.marker = marker
        self.model = model
        self.colour = colour
        self.price = price
        if (not purchase_type in Car.PURCHASE_TYPES):
            raise ValueError(f"{purchase_type} is not in a list ")
        else:
            self.purchase_type = purchase_type

        # что-то вроде частной переменной, но по факту искажение имени(можно получить доступ _classname__spam)
        self.__secret = "tss"

    #getter
    def get_price(self) -> str:
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    #setter
    def set_discount(self, amount) -> None:
        # _ обозначение что это внутриклассовая херь 
        self._discount = amount

class Boat:
    def __init__(self, name) -> None:
        self.name = name

car1 = Car("audi", 'r8', 'red', 13000, 'CASH')
car2 = Car("bmw", 'i8', 'white', 23000, 'CASH')

boat1 = Boat("titanic")

#print(type(car1))
#print(type(boat1))
#print(type(car1) == type(boat1))

#isinstance - является ли экземпляром

#print(isinstance(car1, Car))
#print(isinstance(boat1, Car))
#print(isinstance(boat1, object))

print("<--------------------------->\n")

print(car1.get_purchase_types())
print(car1.purchase_type)

print("<--------------------------->\n")

sales_this_month = Car.get_sales_list()
sales_this_month.append(car1)
sales_this_month.append(car2)

print(sales_this_month)
