#линейное наследование

class Vehicle:
    def __init__(self, marker, model, colour, price) -> None:
        self.marker = marker
        self.model = model
        self.colour = colour
        self.price = price

class Car(Vehicle):
    def __init__(self, marker, model, colour, price, seats) -> None:
        super().__init__(marker, model, colour, price)
        self.seats = seats

class Industrial_Vehicle(Vehicle):
    def __init__(self, marker, model, colour, price, lift_weight) -> None:
        super().__init__(marker, model, colour, price)
        self.lift_weight = lift_weight

class Forklift(Industrial_Vehicle):
    def __init__(self, marker, model, colour, price, lift_weight) -> None:
        super().__init__(marker, model, colour, price, lift_weight)

class Crane(Industrial_Vehicle):
    def __init__(self, marker, model, colour, price, lift_weight) -> None:
        super().__init__(marker, model, colour, price, lift_weight)

car1 = Car("mersedes", "amg gt", 'black', 150000, 2)
Forklift = Forklift("Honda", "foll", "orange", 10000, 10)
crane = Crane("Caterpillar", "cat", "yellow", 64000, 55)

print(car1.marker)
print(Forklift.lift_weight)
print(crane.price)