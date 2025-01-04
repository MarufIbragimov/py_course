class CombustionEngine:
    def __init__(self):
        print('Combustion Engine created')
    
    def change_spark_plug(self):
        pass

class ElectricEngine:
    def __init__(self):
        print('Electric Engine created')

class Vehicle:
    def __init__(self):
        print('Vehicle created')
        self.engine = CombustionEngine()  # use this engine by default

    def start_ignition(self):
        pass 

    def change_tire(self):
        pass

class Car(Vehicle):
    def __init__(self):
        print("Car created")

class Motorcycle(Vehicle):
    def __init__(self):
        print("Motorcycle created")

class LunarRover(Vehicle):
    change_spark_plug = None
    def __init__(self):
        print("Lunar Rover created")
        