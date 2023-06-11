#множественное наследование

class Parent1:
    def __init__(self) -> None:
        super().__init__()
        self.smart = "smart"
        self.hair_colour = 'black'

class Parent2:
    def __init__(self) -> None:
        super().__init__()
        self.hair_colour = 'white'
        self.goodlocking = "goodlocking"

class Child(Parent2, Parent1):
    def __init__(self) -> None:
        super().__init__()

    def traits(self) -> None:
        print(self.goodlocking)
        print(self.smart)
        print(self.hair_colour)
        

child = Child()
child.traits()