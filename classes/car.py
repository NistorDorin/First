class Car:
    # fields/campuri/atribute
    make = 'Dacia'
    model = None
    year = None
    color = None

    #construtor
    def __init__(self, year, color):
        self.year = year
        self.color = color

car = Car()
print(car.color)
print(car.make)

car.make = 'Volvo'
print(car.make)
