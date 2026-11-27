class Car:
    make = "Audi"
# __  Dunder methods
    def __init__(self,name,yom):
        self.name = name
        self.yom = yom

    def drive(self):
        return f"{self.name} looks stunning"

    def autonomous(self):
        return self.drive()

    def __str__(self):
        return f"{self.name} ({self.yom} year)"

    def __repr__(self):
        return f"Car (name={self.name!r}, Yom={self.yom!r})"

c = Car("A4",2026)
print(c.drive(), "|", c, "|", Car.make)
print(repr(c)) #debug
print(Car,type(c))