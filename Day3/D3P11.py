# Composition: 
class Engine:
    def start(self):
        return "engine started"

    def stop(self):
        return "engine stopped"

class Wheels:
    def inflate(self,psi):
        return f"wheels at {psi} psi"

class Car:
    def __init__(self,model):
        self.model = model
        self.engine = Engine() # Car HAS-A engine
        self.wheels = Wheels() # Car HAS-A wheels

    def drive(self):
        return f"{self.model}: {self.engine.start()}, {self.wheels.inflate(32)}"

car = Car("Audi Q3")
print(car.drive())
print(type(car.engine).__name__)