import datetime

class Car:
    def __init__(self, year, make, model):
        self.year = year
        self.make = make
        self.model = model

    def age(self):
        return datetime.datetime.now().year - self.year


myCar = Car(2000, 'Toyota', 'Rav4')

print(myCar.age())