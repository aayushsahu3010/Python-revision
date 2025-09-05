# scopes in python
class Car:
    total_cars = 0  # class variable
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_cars += 1 

    def display(self):
        print(self.__brand, self.model)


my_car = Car("Toyota", "corolla")
print(my_car.brand)
print(my_car.model)


car2 = Car("Honda", "Civic")
print(car2.brand)
print(car2.model)
car2.display()

class ElectricCar(Car):
    def __init__(self, __brand, model,battery_size):
        self.battery_size = battery_size
        super().__init__(__brand, model)
    
        


tesla = ElectricCar("Tesla", "Model S", 100)
print(tesla.brand)
tesla.display()