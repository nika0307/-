class Car:
    def __init__(self, speed, colour, name, is_polise, direction):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.is_polise = is_polise
        self.direction = direction

class TownCar:
    def __init__(self, speed, colour, name, is_polise, direction):
        Car.__init__(self, speed, colour, name, is_polise, direction)

    def go(self):
        return "car's started"

    def stop(self):
        return "Car's stopped"

    def turn(self, direction):
     
        return f"Car turned to the {self.direction}"

class SportCar:
    def __init__(self, speed, colour, name, is_polise, direction):
        Car.__init__(self, speed, colour, name, is_polise, direction)
    
    def go(self):
        return "Car's started"

    def stop(self):
        return "Car's stopped"

    def turn(self, direction):
        
        return f"Car turned to the {self.direction}"

class WorkCar:
    def __init__(self, speed, colour, name, is_polise, direction):
        Car.__init__(self, speed, colour, name, is_police, direction)

    def go(self):
        return "Car's started"

    def stop(self):
        return "stopped"

    def turn(self, direction):
        
        return f"Car turned to the {self.direction}"

class PoliceCar:
    def __init__(self, speed, colour, name, is_polise, direction):
        Car.__init__(self, speed, colour, name, is_police, direction)

    def go(self):
        return "Car's started"

    def stop(self):
        return "stopped"

    def turn(self, direction):
        
        return f"Car turned to the {self.direction}"

car1 = TownCar("322", "blue", "BMW", True)
print(car1.go(), car1.stop(), car1.turn("left"))
